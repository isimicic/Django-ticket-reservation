from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
import os
from django.db.models import Avg
import datetime


def get_image_path(instance, filename):
    """
    Get movie image path

    :param instance: Get movie title
    :param filename: Get name of the movie file
    :return: path to the movie image
    """
    return os.path.join('images/movie', str(instance.title), filename)


class Category(models.Model):
    """Create category for the movie"""
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
    """Create movie model"""
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(424, 424)],
                                     format='JPEG',
                                     options={'quality': 60})
    title = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    release_date = models.DateTimeField(blank=True, null=True)
    now_playing = models.NullBooleanField()
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    age_restriction = models.CharField(max_length=2, null=True, blank=True)

    objects = MovieManager()

    def get_avg_rating(self):
        """Returns the average rating for a Movie."""
        if self.rated_movie.all():
            return self.rated_movie.aggregate(Avg('rating'))['rating__avg']
        else:
            return 0.00

    def get_rating_votes_today(self):
        """Returns today's rating votes for a Movie"""
        return self.rated_movie.all().filter(
            date_rated__date=datetime.datetime.now().date()).count()

    def __unicode__(self):
        return u"Name: {0}, Director: {1}".format(self.title, self.director)


class City(models.Model):
    """Create City for the movie"""
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.name)


class Cinema(models.Model):
    """Create Cinema """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    CHOICES = [(i, i) for i in range(1, 21, 1)]
    auditorium_number = models.PositiveSmallIntegerField(choices=CHOICES)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return u"{0} {1} {2}".format(
            self.name, self.address, self.auditorium_number)


class Auditorium(models.Model):
    """Create Auditorium """
    name = models.CharField(max_length=255)
    seats_number = models.CharField(max_length=2)
    cinema = models.ForeignKey(Cinema)

    def __unicode__(self):
        return u"{0}, {1}".format(self.cinema.name, self.name)


class ReservationType(models.Model):
    """Create Reservation Type"""
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.type)


class ScreeningManager(models.Manager):
    """Create Screening Manager"""
    # queryset = Screening.objects.filter(
    #    auditorium__cinema__city__id=request.POST['cityId'])

    def getScreenings(self, cityId, movieId):
        import time
        from django.utils import timezone
        data = []
        movie = Movie.objects.get(pk=movieId)
        print movie
        queryset = self.all().filter(
            movie=movie,
            auditorium__cinema__city__id=cityId
        ).order_by('auditorium__cinema__name')
        for screening in queryset.filter(
                screening_start__gte=timezone.localtime(timezone.now())):

            start = screening.screening_start
            end = screening.screening_end

            data.append({
                'screeningId': screening.id,
                'cinemaId': screening.auditorium.cinema.id,
                'cinemaName': screening.auditorium.cinema.name,
                'auditoriumId': screening.auditorium.id,
                'start': int(
                    time.mktime(start.timetuple()) * 1000),
                'end': int(time.mktime(end.timetuple()) * 1000),
            })
        return {'success': 1, 'data': data}


class Screening(models.Model):
    """Create Screening"""
    objects = ScreeningManager()

    screening_start = models.DateTimeField()
    screening_end = models.DateTimeField()
    movie = models.ForeignKey(Movie)
    auditorium = models.ForeignKey(Auditorium)

    def __unicode__(self):
        return u"{0} {1}".format(self.screening_start, self.screening_end)


class Seat(models.Model):
    """Create Seat"""
    rowNumber = models.CharField(max_length=3)
    screenings = models.ForeignKey(Screening)

    def __unicode__(self):
        return u"{0}".format(self.rowNumber)

    class Meta:
        unique_together = ("rowNumber", "screenings")


class Reservation(models.Model):
    """Create Reservation"""
    reservation_date = models.DateTimeField(auto_now=True)
    reserved = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    reservation_type = models.ForeignKey(ReservationType)
    user = models.ForeignKey(User)
    screening = models.ForeignKey(Screening)
    seat = models.ManyToManyField(Seat)
    amount = models.DecimalField(max_digits=5, decimal_places=2,
                                 null=True, blank=True)

    def __unicode__(self):
        return u"{0} {1} {2} {3}".format(
            self.reservation_date, self.reserved, self.paid, self.active)
