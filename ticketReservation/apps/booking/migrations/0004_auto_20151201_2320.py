# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20151201_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='auditorium_number',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='seat',
            name='number',
            field=models.PositiveSmallIntegerField(choices=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20)]),
        ),
    ]
