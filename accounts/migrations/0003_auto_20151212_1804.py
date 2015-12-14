# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 17:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151212_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User_profile', to=settings.AUTH_USER_MODEL, verbose_name=b'user'),
        ),
    ]
