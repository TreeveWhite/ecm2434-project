'''


'''

from django.db import models

class Users(models.Model):
    name = models.TextField()
    user_username = models.TextField()
    user_password = models.TextField()

class Locations(models.Model):
    name = models.TextField()
    p1_longitude = models.IntegerField()
    p1_latitude = models.IntegerField()
    p2_longitude = models.IntegerField()
    p2_latitude = models.IntegerField()
    claimedBy = models.ForeignKey("Users", on_delete=models.SET_NULL, null=True)


