# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_reservation_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='auditorium',
        ),
        migrations.AddField(
            model_name='seat',
            name='screenings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.Screening'),
            preserve_default=False,
        ),
    ]
