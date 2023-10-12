from django.contrib import admin
from .models import Image, ExpiringLink, ThumbnailSize

admin.site.register(Image)
admin.site.register(ExpiringLink)
admin.site.register(ThumbnailSize)
