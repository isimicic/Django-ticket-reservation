# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('seats_number', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('auditorium_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('cast', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reserved', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('screening_start', models.DateTimeField()),
                ('auditorium', models.ForeignKey(to='booking.Auditorium')),
                ('movie', models.ForeignKey(to='booking.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.CharField(max_length=2)),
                ('number', models.CharField(max_length=2)),
                ('auditorium', models.ForeignKey(to='booking.Auditorium')),
            ],
        ),
        migrations.CreateModel(
            name='SeatReserved',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Screening', models.ForeignKey(to='booking.Screening')),
                ('reservation', models.ForeignKey(to='booking.Reservation')),
                ('seat', models.ForeignKey(to='booking.Seat')),
            ],
        ),
        migrations.AddField(
            model_name='screening',
            name='reserved_seats',
            field=models.ManyToManyField(to='booking.Seat', through='booking.SeatReserved'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_type',
            field=models.ForeignKey(to='booking.ReservationType'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cinema',
            name='city',
            field=models.ForeignKey(to='booking.City'),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='cinema',
            field=models.ForeignKey(to='booking.Cinema'),
        ),
    ]
