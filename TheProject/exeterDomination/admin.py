from django.contrib import admin

from exeterDomination.models import Locations, CoOrds

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    pass

@admin.register(CoOrds)
class CoOrdsAdmin(admin.ModelAdmin):
    pass
