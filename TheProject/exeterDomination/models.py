'''


'''

from django.db import models


class Users(models.Model):
    name = models.TextField()
    username = models.TextField()
    password = models.TextField()

class Locations(models.Model):
    name = models.TextField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    claimedBy = models.IntegerField()


