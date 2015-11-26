from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=5)

    def __unicode__(self):
        return "{0} {1} {2} {3} {4} {5}".format(
            self, self.title, self.director, self.cast,
            self.description, self.duration)


class City(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0} {1}".format(self, self.name)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    auditorium_number = models.CharField(max_length=100)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return "{0} {1} {2} {3}".format(
            self, self.name, self.address, self.auditorium_number)


class Auditorium(models.Model):
    name = models.CharField(max_length=255)
    seats_number = models.CharField(max_length=2)
    cinema = models.ForeignKey(Cinema)

    def __unicode__(self):
        return "{0} {1} {2}".format(self, self.name, self.seats_number)


class Seat(models.Model):
    row = models.CharField(max_length=2)
    number = models.CharField(max_length=2)
    auditorium = models.ForeignKey(Auditorium)

    def __unicode__(self):
        return "{0} {1} {2}".format(self, self.row, self.number)


class ReservationType(models.Model):
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0} {1}".format(self, self.type)


class Reservation(models.Model):
    reservation_date = models.DateTimeField(default=datetime.now)
    reserved = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    reservation_type = models.ForeignKey(ReservationType)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{0} {1} {2} {3} {4}".format(
            self, self.reservation_date, self.reserved, self.paid, self.active)


class Screening(models.Model):
    screening_start = models.DateTimeField()
    movie = models.ForeignKey(Movie)
    auditorium = models.ForeignKey(Auditorium)
    reserved_seats = models.ManyToManyField(Seat, through='SeatReserved')

    def __unicode__(self):
        return "{0} {1}".format(self, self.screening_start)


class SeatReserved(models.Model):
    reservation = models.ForeignKey(Reservation)
    seat = models.ForeignKey(Seat)
    Screening = models.ForeignKey(Screening)
