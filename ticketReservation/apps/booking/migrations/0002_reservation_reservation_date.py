# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
