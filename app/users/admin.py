from django.contrib import admin

from .models import MyUser, AccountTier

admin.site.register(MyUser)
admin.site.register(AccountTier)
