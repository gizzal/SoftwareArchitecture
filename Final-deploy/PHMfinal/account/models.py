from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def fullname(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Config(models.Model):
    """ Configuration data of the service """
    broker_ip = models.CharField(max_length=50)
    broker_http_port = models.CharField(max_length=50)
    broker_ws_port = models.CharField(max_length=50)
