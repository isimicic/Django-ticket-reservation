# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_movie_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='age_restriction',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
