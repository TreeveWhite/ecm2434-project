"""
admin.py
=======================================
This module contains the classes which register Locations and Coord to the
django Admin framework which allows superusers to modify and edit data sorted in
the database tables created from the models.
"""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import SafeString
from exeterDomination.models import Locations, CoOrds
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = [
        'id',
        'username',
        'is_active',
        'date_joined',
        'is_staff',
        "claimedBy"]

    def claimedBy(self, obj):
        url = (
            reverse("admin:exeterDomination_locations_changelist")
            + "?"
            + urlencode({"claimedBy_id": obj.id})
        )
        return format_html('<a href="{}">{} Locations Claimed</a>', url,
                           len(Locations.objects.filter(claimedBy_id=obj.id)))


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    """
    This class is required to register the Locations Model with the Django Admin.
    This therefore allows any superusers (Game Keepers) acessing the project via
    the admin page to modify the Locations in the database.
    """
    list_display = (
        "name",
        "topRightCoordinate",
        "bottomLeftCoordinate",
        "claimedLink",
    )

    def claimedLink(self, obj):
        url = (
            reverse("admin:auth_user_changelist")
            + "?"
            + urlencode({"username": f"{obj.claimedBy}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.claimedBy)

    claimedLink.short_description = "Claimed By"


@admin.register(CoOrds)
class CoOrdsAdmin(admin.ModelAdmin):
    """
    This class is required to register the Coord Model with the Django Admin.
    This therefore allows any superusers (Game Keepers) acessing the project via
    the admin page to modify the Coord in the database.
    """
    list_display = ("id", "longitude", "latitude", "linked_location")

    def linked_location(self, obj) -> SafeString:
        if len(Locations.objects.filter(bottomLeftCoordinate_id=obj.id)) == 1:
            url = (
                reverse("admin:exeterDomination_locations_changelist")
                + "?"
                + urlencode({"bottomLeftCoordinate_id": f"{obj.id}"})
            )
            return format_html(
                '<a href="{}">{}</a>',
                url,
                Locations.objects.get(
                    bottomLeftCoordinate=obj.id).name)
        elif len(Locations.objects.filter(topRightCoordinate_id=obj.id)):
            url = (
                reverse("admin:exeterDomination_locations_changelist")
                + "?"
                + urlencode({"topRightCoordinate_id": f"{obj.id}"})
            )
            return format_html(
                '<a href="{}">{}</a>',
                url,
                Locations.objects.get(
                    topRightCoordinate_id=obj.id).name)

    pass
