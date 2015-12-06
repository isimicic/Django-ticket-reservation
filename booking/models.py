from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    cast = models.TextField()
    description = models.TextField()
    duration = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4}".format(
            self.title, self.director, self.cast,
            self.description, self.duration)


class City(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.name)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    CHOICES = [(i, i) for i in range(1, 21, 1)]
    auditorium_number = models.PositiveSmallIntegerField(choices=CHOICES)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return u"{0} {1} {2}".format(
            self.name, self.address, self.auditorium_number)


class Auditorium(models.Model):
    name = models.CharField(max_length=255)
    seats_number = models.CharField(max_length=2)
    cinema = models.ForeignKey(Cinema)

    def __unicode__(self):
        return u"{0} {1}".format(self.name, self.seats_number)


class Seat(models.Model):
    row = models.CharField(max_length=2)
    CHOICES = [(i, i + 1) for i in range(20)]
    number = models.PositiveSmallIntegerField(choices=CHOICES)
    auditorium = models.ForeignKey(Auditorium)

    def __unicode__(self):
        return u"{0} {1}".format(self.row, self.number)


class ReservationType(models.Model):
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.type)


class Screening(models.Model):
    screening_start = models.DateTimeField()
    movie = models.ForeignKey(Movie)
    auditorium = models.ForeignKey(Auditorium)

    def __unicode__(self):
        return u"{0}".format(self.screening_start)


class Reservation(models.Model):
    reservation_date = models.DateTimeField(default=datetime.now)
    reserved = models.BooleanField(default=True)
    paid = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    reservation_type = models.ForeignKey(ReservationType)
    user = models.ForeignKey(User)
    screening = models.ForeignKey(Screening)
    seat = models.ManyToManyField(Seat)

    def __unicode__(self):
        return u"{0} {1} {2} {3}".format(
            self.reservation_date, self.reserved, self.paid, self.active)