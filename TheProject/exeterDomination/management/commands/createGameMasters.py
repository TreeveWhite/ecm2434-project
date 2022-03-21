from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from exeterDomination.models import Locations, CoOrds


class Command(BaseCommand):
    def handle(self, *args, **options):
        newGroup, created = Group.objects.get_or_create(name="Game Masters")
        coordsCT = ContentType.objects.get_for_model(CoOrds)
        locationsCT = ContentType.objects.get_for_model(Locations)

        if created:
            perm1 = Permission.objects.create(codename="can_add_locations", name="Can add locations", content_type=locationsCT)
            perm2 = Permission.objects.create(codename="can_view_locations", name="Can view locations", content_type=locationsCT)
            perm3 = Permission.objects.create(codename="can_add_coords", name="Can add coords", content_type=coordsCT)
            perm4 = Permission.objects.create(codename="can_view_coords", name="Can view coords", content_type=coordsCT)

            newGroup.permissions.add(perm1)
            newGroup.permissions.add(perm2)
            newGroup.permissions.add(perm3)
            newGroup.permissions.add(perm4)

            newGroup.save()
            print("Success")
        else:
            print("Done")
            pass