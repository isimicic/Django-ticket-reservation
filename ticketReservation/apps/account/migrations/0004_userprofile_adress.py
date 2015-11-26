# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20151125_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='adress',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
