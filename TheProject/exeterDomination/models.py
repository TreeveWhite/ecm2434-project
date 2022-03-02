from django.conf import settings
from django.db import models


class Locations(models.Model):

    name = models.TextField()

    trCoOrd = models.ForeignKey(
        'CoOrds',
        on_delete=models.SET_NULL,
        null=True,
        related_name='topRigh')

    blCoOrd = models.ForeignKey(
        'CoOrds',
        on_delete=models.SET_NULL,
        null=True,
        related_name='bottomLeft')

    claimedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True)

    def __str__(self) -> str:
        return f"{self.name}"
    



class CoOrds(models.Model):

    longitude = models.DecimalField(decimal_places=6, max_digits=8)

    latitude = models.DecimalField(decimal_places=6, max_digits=8)

    def __str__(self) -> str:
        return f"Long: {self.longitude}, Lat: {self.latitude}"