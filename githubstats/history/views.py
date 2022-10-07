import math
import random
from datetime import datetime, timedelta

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from .models import Visit

# A list of ui gradients to stylize the header image.
# The gradients are taken from https://uigradients.com/
ui_gradients = [
    ('#4e54c8', '#8f94fb'),
    ('#f12711', '#f5af19'),
    ('#7F00FF', '#E100FF'),
    ('#396afc', '#2948ff'),
    ('#ff9966', '#ff5e62'),
    ('#ee0979', '#ff6a00'),
    ('#cb2d3e', '#ef473a'),
    ('#e52d27', '#b31217'),
]


def line(point_a, point_b):
    length_x = point_b[0] - point_a[0]
    length_y = point_b[1] - point_a[1]
    return {
        'length': (length_x ** 2 + length_y ** 2) ** 0.5,
        'angle': math.atan2(length_y, length_x),
    }


def control_point(current, previous, next, reverse=False):
    p = previous or current
    n = next or current
    smoothing = 0.2
    o = line(p, n)
    angle = o['angle'] + (math.pi if reverse else 0)
    length = o['length'] * smoothing
    x = current[0] + math.cos(angle) * length
    y = current[1] + math.sin(angle) * length
    return [x, y]


def bezier_command(point, i, points):
    cps = control_point(points[i - 1], points[i - 2], point)
    cpe = control_point(point, points[i - 1], points[i + 1], True)
    return f'C {cps[0]},{cps[1]} {cpe[0]},{cpe[1]} {point[0]},{point[1]}'


def make_bezier_path(points, start_point=None, end_point=None):
    path = ''
    for i, point in enumerate(points):
        if i == 0:
            if start_point:
                path += f'M {start_point[0]},{start_point[1]} '
            path += f'L {point[0]} {point[1]} '
        elif i == 1:
            path += f'L {point[0]} {point[1]} '
        elif i == len(points) - 1:
            path += f'L {point[0]} {point[1]} '
            if end_point:
                path += f'L {end_point[0]},{end_point[1]} '
        else:
            path += f' {bezier_command(point, i, points)}'
    return path


class HeaderView(View):
    """
    A resource that provides an animated SVG for the GitHub readme.

    This works as follows: First, we log a visit object to the database. Then,
    we get the history of visits. Finally, we render an SVG template.
    """

    @method_decorator(never_cache, name='dispatch') # Avoid image caching by GitHub.
    def get(self, request):
        # Create a visit object in the database.
        visit = Visit.objects.create()

        # For debugging: Create visits for the last 30 days.
        n_visits = ordinal(Visit.objects.count())

        # Get the visits, grouped by day for the last n days.
        start_date = datetime.now() - timedelta(days=7)
        visits = Visit.objects \
            .filter(date__gte=start_date, date__lte=visit.date) \
            .annotate(day=TruncDay('date')) \
            .values('day') \
            .annotate(count=Count('pk')) \
            .order_by('day')

        # Select a random gradient from the list.
        gradient_stop_1, gradient_stop_2 = random.choice(ui_gradients)

        # Generate a <path> element which is a line graph of the visits.
        # The path should start at the left center of the image and end at the
        # right center of the image.
        viewport_width = 1920
        viewport_height = 1080
        x_start = viewport_width / 4
        x_end = viewport_width - x_start
        x_step = (x_end - x_start) / (len(visits) - 1)
        y_min = viewport_height / 4
        y_max = viewport_height - y_min
        y_mid = viewport_height / 2
        y_range = y_max - y_min
        # Scale the y axis to the range of the visits.
        max_visits = max([visit['count'] for visit in visits])
        min_visits = 0
        y_scale = y_range / (max_visits - min_visits)

        # Draw a bezier line graph of the visits.
        points = []
        for i, visit in enumerate(visits):
            x = x_start + i * x_step
            # Scale y between y_max and y_min.
            y = y_max - (visit['count'] - min_visits) * y_scale
            points.append([x, y])
        path = make_bezier_path(points, start_point=[x_start, y_mid], end_point=[x_end, y_mid])

        # Draw an initial line graph which is used to animate the bezier line
        # graph. The initial line graph is a straight line from the left center
        # to the right center. However, it needs to contain the same number of
        # points as the bezier line graph.
        initial_points = []
        for i in range(len(points)):
            x = x_start + i * x_step
            initial_points.append([x, y_mid])
        initial_path = make_bezier_path(initial_points, start_point=[x_start, y_mid], end_point=[x_end, y_mid])
        
        # Generate dots for each visit.
        dots = ''
        for i, visit in enumerate(visits):
            x = x_start + i * x_step
            y = y_max - (visit['count'] - min_visits) * y_scale
            dots += f'<circle class="dot" cx="{x}" cy="{y}" r="12" fill="{gradient_stop_2}" />'
        
        svg = render_to_string('header.svg', { 
            'initial_path': initial_path,
            'path': path,
            'dots': dots,
            'gradient_stop_1': gradient_stop_1,
            'gradient_stop_2': gradient_stop_2,
            'n_visits': n_visits,
        })
        return HttpResponse(svg, content_type='image/svg+xml')
