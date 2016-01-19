import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
import os


def get_image_path(instance, filename):
    """
    Get image path

    :param instance: Get user's username
    :param filename: Get name of the image file
    :return: path to the user's image
    """
    return os.path.join('img', str(instance.user.username), filename)


class User_profile(models.Model):
    """
    Create User Profile
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, unique=True,
                                verbose_name=('user'),
                                related_name='User_profile')
    image = ProcessedImageField(upload_to=get_image_path,
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 60}, blank=True,
                                null=True)

    def __unicode__(self):
        return u"{0}".format(self.user.username)
