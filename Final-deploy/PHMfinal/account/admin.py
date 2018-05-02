from django.contrib import admin

from account.models import Profile, Config

admin.site.register(Profile)
admin.site.register(Config)
