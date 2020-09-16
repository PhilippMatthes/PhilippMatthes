from django.views import View
from django.http import Http404, HttpResponse
from django.views.decorators.cache import never_cache

from .models import Chart
from .tasks import update_history


class ChartView(View):
    @never_cache
    def get(self, request):
        old_chart = Chart.objects.order_by('-date').first()
        update_history(old_chart)
        if not old_chart:
            raise Http404
        return HttpResponse(old_chart.image.read(), content_type='image/png')
