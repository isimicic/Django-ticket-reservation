# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20151213_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(default='zagreb', max_length=255),
            preserve_default=False,
        ),
    ]