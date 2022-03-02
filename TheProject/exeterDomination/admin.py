"""
admin.py
=======================================
This module contains the classes which register Locations and CoOrds to the 
django Admin framework which allows suprusers to modify and edit data sorted in
the database tables created from the models.
"""

from django.contrib import admin

from exeterDomination.models import Locations, CoOrds


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    """
    This class is required to register the Locations Model with the Django Admin.
    This therefore allows any superusers (Game Keepers) acessing the project via
    the admin page to modify the Locations in the database.
    """
    pass


@admin.register(CoOrds)
class CoOrdsAdmin(admin.ModelAdmin):
    """
    This class is required to register the CoOrds Model with the Django Admin.
    This therefore allows any superusers (Game Keepers) acessing the project via
    the admin page to modify the CoOrds in the database.
    """
    pass
