import matplotlib

from io import BytesIO
from datetime import datetime, timedelta

from django.db.models.functions import TruncDay
from django.db.models import Count, Max
from django.core.files.uploadedfile import SimpleUploadedFile

import pandas as pd
import numpy as np

from huey.contrib.djhuey import db_task
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib import colors as mcolors

from .models import Chart, Visit


def make_colormap(seq):
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)


cmap_converter = mcolors.ColorConverter().to_rgb
cmap = make_colormap([cmap_converter('white'), cmap_converter('#0072ff')])
fmt = mdates.DateFormatter('%b %Y')
loc = mdates.MonthLocator()
bbox = dict(boxstyle='round', ec='w', fc='w', alpha=0.5)


@db_task()
def update_history(old_chart):
    visit = Visit.objects.create()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 6))

    start_date = datetime.now() - timedelta(days=270)

    visits = Visit.objects \
        .filter(date__gte=start_date, date__lte=visit.date) \
        .annotate(day=TruncDay('date')) \
        .values('day') \
        .annotate(count=Count('pk')) \
        .order_by('day')

    df = pd.DataFrame(visits)
    mean = df['count'].mean()
    std = df['count'].std()

    df['weekday'] = df['day'].apply(lambda day: day.weekday())
    df['order'] = df['day'].apply(lambda day: (day.year * 100) + day.week)
    df = df.pivot(columns='order', index='weekday', values='count')
    df = df.fillna(0)

    ax1.imshow(df.values, cmap=cmap, vmax=std+mean)

    ax1.set_yticks(np.arange(7))
    ax1.set_xticks([])
    ax1.set_yticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            value = df.values[i, j]
            color = 'k' if value < mean else 'w'
            ax1.text(
                j, i,
                int(df.values[i, j]),
                ha='center',
                va='center',
                color=color
            )

    ax2.xaxis.set_major_formatter(fmt)
    ax2.xaxis.set_major_locator(loc)
    x = [d['day'] for d in visits]
    y = [d['count'] for d in visits]
    ax2.plot(x, y, color='#0072ff')
    ax2.fill_between(x, 0, y, color='#0072ff', alpha=0.2)
    ax2.set_xlim(min(x) - timedelta(days=4.5), max(x) + timedelta(days=4.5))
    ax2.set_ylim(0, max(y))
    ax2.grid(True)
    fig.autofmt_xdate()

    plt.tight_layout()

    plt.setp(ax1.get_yticklabels(), bbox=bbox)
    plt.setp(ax2.get_yticklabels(), bbox=bbox)
    plt.setp(ax2.get_xticklabels(), bbox=bbox)

    buf = BytesIO()
    fig.savefig(buf, format='png', transparent=True)
    image = SimpleUploadedFile(
        name='line.png',
        content=buf.getvalue(),
        content_type='image/png'
    )
    buf.close()
    plt.close(fig)

    new_chart = Chart.objects.create(type='line', image=image)
    Chart.objects.exclude(pk__in=[new_chart.pk, old_chart.pk]).delete()
