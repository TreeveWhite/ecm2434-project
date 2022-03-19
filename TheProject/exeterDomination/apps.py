"""
alarms.py
=======================================
This module contains the ExeterdominationConfit class that enables django to see the
exeterDomination app as an app in the system.
"""
from django.apps import AppConfig


class ExeterdominationConfig(AppConfig):
    """
    This class is the confirguration class for the exeterDomination app and
    specifies the defult_auto_field attribute and the name attribute.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exeterDomination'
