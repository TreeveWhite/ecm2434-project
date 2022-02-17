'''


'''

from django.db import models

class Users(models.Model):
    name = models.TextField()
    username = models.TextField()
    password = models.TextField()

class Locations(models.Model):
    name = models.TextField()
    p1Longitude = models.IntegerField()
    p1Latitude = models.IntegerField()
    p2Longitude = models.IntegerField()
    p2Latitude = models.IntegerField()
    claimedBy = models.ForeignKey("Users", on_delete=models.SET_NULL, null=True)


