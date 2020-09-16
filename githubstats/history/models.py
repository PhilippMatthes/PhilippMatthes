import os

from contextlib import suppress

from django.utils.text import slugify
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver


def chart_image_upload_path(instance, filename):
    return f'charts/{slugify(instance.date)}_{filename}'


class Chart(models.Model):
    type = models.TextField()
    image = models.ImageField(upload_to=chart_image_upload_path)
    date = models.DateTimeField(default=timezone.now)


@receiver(post_delete, sender=Chart, dispatch_uid='delete_image')
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        with suppress(PermissionError):
            os.remove(instance.image.path)


class Visit(models.Model):
    date = models.DateTimeField(default=timezone.now)
