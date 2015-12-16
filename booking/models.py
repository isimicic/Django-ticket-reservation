from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
import os
from django.db.models import Avg


def get_image_path(instance, filename):
    return os.path.join('images/movie', str(instance.title), filename)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.name)


class MovieManager(models.Manager):
    """Adds custom methods to Show model."""
    def top_rated(self):
        try:
            return self.annotate(score=Avg(
                'rated_movie__rating')).order_by('-score')
        except Exception:
            return self

    def most_rated(self):
        return self.annotate(score=Avg('rated_movie')).order_by('-score')


class Movie(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(424, 424)],
                                     format='JPEG',
                                     options={'quality': 60})
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    cast = models.TextField()
    description = models.TextField()
    duration = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    release_date = models.DateTimeField()
    now_playing = models.BooleanField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age_restriction = models.CharField(max_length=2, null=True, blank=True)

    objects = MovieManager()

    def get_avg_rating(self):
        """Returns the average rating for a Movie."""
        if self.rated_movie.all():
            return self.rated_movie.aggregate(Avg('rating'))['rating__avg']
        else:
            return 0.00

    def get_rating_votes(self):
        """Returns all rating votes for a show."""
        return self.rated_movie.all().count()

    def __unicode__(self):
        return u"Name: {0}, Director: {1}".format(self.title, self.director)


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
    screening_end = models.DateTimeField()
    movie = models.ForeignKey(Movie)
    auditorium = models.ForeignKey(Auditorium)

    def __unicode__(self):
        return u"{0} {1}".format(self.screening_start, self.screening_end)


class Reservation(models.Model):
    reservation_date = models.DateTimeField(auto_now=True)
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
