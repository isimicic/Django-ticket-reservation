# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofile_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='adress',
            new_name='address',
        ),
    ]
