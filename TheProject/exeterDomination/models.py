'''


'''

from django.db import models

class Users(models.Model):
    username = models.TextField()
    password = models.TextField()

class Locations(models.Model):
    name = models.TextField()
    trCoOrd = models.ForeignKey('CoOrds', on_delete=models.SET_NULL, null=True, related_name='topRigh')
    blCoOrd = models.ForeignKey('CoOrds', on_delete=models.SET_NULL, null=True, related_name='bottomLeft') 
    claimedBy = models.ForeignKey("Users", on_delete=models.SET_NULL, null=True)

class CoOrds(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()