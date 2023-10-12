import uuid

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from .validators import validate_expiration_time

UserModel = get_user_model()


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_file = models.FileField(upload_to='images/', validators=[FileExtensionValidator(['jpg', 'png'])])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='images')


class ExpiringLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ForeignKey('images.Image', on_delete=models.CASCADE, related_name='expiring_link')
    expiration_time = models.IntegerField(default=300, validators=[validate_expiration_time])
    expiration_datetime = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return self.link


class ThumbnailSize(models.Model):
    height = models.IntegerField()
    width = models.IntegerField(default=0)

    def __str__(self):
        return f'Thumbnail({self.height}x{self.width})'
