from django.db import models
from django.contrib.auth.models import User, UserManager
from django.core.validators import RegexValidator


class UserProfile(User):
    """ User Profile Model """
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'.\
        Up to 15 digits allowed")
    number = models.CharField(max_length=15, validators=[phone_regex])
    address = models.CharField(max_length=50, default=None)

    def __unicode__(self):
        """Return nicely formatted address."""
        return u'{0} {1} {2}'.format(self, self.number, self.address)

    objects = UserManager()
