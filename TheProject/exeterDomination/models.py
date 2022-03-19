"""
models.py
=======================================
This module creates the database models for
the coordinates and locations tables.
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Locations(models.Model):
    """
    This is the class which inherits from models.Model and is used
    to create a model for all the Locations in the Server.

    Django then uses this class to create a table in the database.

    The attribute of Locations (each column in the table are):

    * name - name of location
    * trCoOrd - Top Right Coordinate
    * blBoOrd - Bottom Right Coordinate
    * claimedBy - The User which has claimed the location.
    """

    name = models.TextField()

    topRightCoordinate = models.ForeignKey(
        'CoOrds',
        on_delete=models.SET_NULL,
        null=True,
        related_name='topRigh',
        verbose_name="Top Right Coordinate")

    bottomLeftCoordinate = models.ForeignKey(
        'CoOrds',
        on_delete=models.SET_NULL,
        null=True,
        related_name='bottomLeft',
        verbose_name="Bottom Left Coordinate")

    claimedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Claimed By")

    def __str__(self) -> str:
        """
        This function returns the Location in a neat
        string format.
        """
        return f"{self.name}"

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class CoOrds(models.Model):
    """
    This is the class which inherits from models.Model and is used
    to create a model for all the Coord in the Server.

    Django then uses this class to create a table in the database.

    The attribute of Coord (each column in the table are):

    * longitude - the longitudinal value
    * latitude - the latitudinal value
    """

    longitude = models.DecimalField(decimal_places=6, max_digits=8)

    latitude = models.DecimalField(decimal_places=6, max_digits=8)

    def __str__(self) -> str:
        """
        This function returns the Coord in a neat
        string format.
        """
        return f"Long: {self.longitude}, Lat: {self.latitude}"

    class Meta:
        verbose_name = _("Coordinate")
        verbose_name_plural = _("Coordinates")
