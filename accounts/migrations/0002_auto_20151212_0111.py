# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 00:11
from __future__ import unicode_literals

import accounts.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=accounts.models.get_image_path),
        ),
    ]
