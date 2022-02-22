'''


'''

from django.db import models

class Users(models.Model):
    username = models.TextField()
    password = models.TextField()
    lastPos = models.ForeignKey('CoOrds', on_delete=models.SET_NULL, null=True)

class Locations(models.Model):
    name = models.TextField()
    trCoOrd = models.ForeignKey('CoOrds', on_delete=models.SET_NULL, null=True)
    blCoOrd = models.ForeignKey('CoOrds', on_delete=models.SET_NULL, null=True) 
    claimedBy = models.ForeignKey("Users", on_delete=models.SET_NULL, null=True)

class CoOrds(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()