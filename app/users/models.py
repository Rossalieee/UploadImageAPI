import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class AccountTier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    allow_expiring_link = models.BooleanField(default=False)
    allow_original_image = models.BooleanField(default=False)
    thumbnail_sizes = models.ManyToManyField('images.ThumbnailSize', related_name='account_tiers')

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tier = models.ForeignKey('users.AccountTier', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
