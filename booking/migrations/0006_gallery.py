# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 14:27
from __future__ import unicode_literals

import booking.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20151213_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=booking.models.get_image_path)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Movie')),
            ],
        ),
    ]
