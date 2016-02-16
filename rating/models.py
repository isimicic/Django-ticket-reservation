from django.contrib.auth.models import User
from django.db import models
from booking.models import Movie

RATING_CHOICES = (
    (1, 'bad'),
    (2, 'poor'),
    (3, 'regular'),
    (4, 'good'),
    (5, 'gorgeus'),)


class Rating(models.Model):
    """Rating model for Show model."""
    movie = models.ForeignKey(Movie, related_name='rated_movie')
    user = models.ForeignKey(User, related_name='user_rated')
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    date_rated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0} rated {1} {2}".format(self.user, self.movie,
                                           self.get_rating_display())

    class Meta:
        unique_together = ("movie", "user"),
