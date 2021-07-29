import matplotlib

from io import BytesIO

from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.files.uploadedfile import SimpleUploadedFile

from huey.contrib.djhuey import db_task
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

from .models import Chart, Visit


matplotlib.use('agg')
plt.rcParams['axes.edgecolor'] = '#333F4B'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['xtick.color'] = '#333F4B'
plt.rcParams['ytick.color'] = '#333F4B'
fmt = mdates.DateFormatter('%Y-%m-%d')
loc = mdates.WeekdayLocator(byweekday=mdates.MONDAY)


@db_task()
def update_history(old_chart):
    visit = Visit.objects.create()

    fig = plt.figure(figsize=(12, 6))
    ax = plt.axes()
    ax.xaxis.set_major_formatter(fmt)
    ax.xaxis.set_major_locator(loc)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    n_visits_per_day = Visit.objects \
        .filter(date__year=visit.date.year) \
        .annotate(day=TruncDay('date')) \
        .values('day') \
        .annotate(count=Count('pk'))

    x = []
    y = []
    for data in n_visits_per_day:
        x.append(data['day'])
        y.append(data['count'])
    plt.bar(x, y, color='#0072ff')
    fig.autofmt_xdate()

    buf = BytesIO()
    fig.savefig(buf, format='png')
    image = SimpleUploadedFile(
        name='line.png',
        content=buf.getvalue(),
        content_type='image/png'
    )
    buf.close()
    plt.close(fig)

    new_chart = Chart.objects.create(
        type='line',
        image=image
    )
    Chart.objects.exclude(pk__in=[new_chart.pk, old_chart.pk]).delete()
