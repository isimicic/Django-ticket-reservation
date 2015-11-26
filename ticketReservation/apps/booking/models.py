from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=5)


class City(models.Model):
    name = models.CharField(max_length=255)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    auditorium_number = models.CharField(max_length=100)
    city = models.ForeignKey(City)


class Auditorium(models.Model):
    name = models.CharField(max_length=255)
    seats_number = models.CharField(max_length=2)
    cinema = models.ForeignKey(Cinema)


class Seat(models.Model):
    row = models.CharField(max_length=2)
    number = models.CharField(max_length=2)
    auditorium = models.ForeignKey(Auditorium)


class ReservationType(models.Model):
    type = models.CharField(max_length=255)


class Reservation(models.Model):
    reservation_date = models.DateTimeField(default=datetime.now)
    reserved = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    reservation_type = models.ForeignKey(ReservationType)
    user = models.ForeignKey(User)


class Screening(models.Model):
    screening_start = models.DateTimeField()
    movie = models.ForeignKey(Movie)
    auditorium = models.ForeignKey(Auditorium)
    reserved_seats = models.ManyToManyField(Seat, through='SeatReserved')


class SeatReserved(models.Model):
    reservation = models.ForeignKey(Reservation)
    seat = models.ForeignKey(Seat)
    Screening = models.ForeignKey(Screening)
