from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    """ User Profile Model """
    user = models.OneToOneField(User, primary_key=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed")
    number = models.CharField(max_length=15, validators=[phone_regex])

User.profile = property(lambda u: UserProfile.objects.get_orcreate(user=u)[0])
