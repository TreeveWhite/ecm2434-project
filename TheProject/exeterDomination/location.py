from django.contrib.auth.models import User
from exeterDomination.models import Locations


def posInRec(userID : int, posLat: int, posLong: int) -> bool:
    """
    This function is used to check if a position is within a rectangle defined by its top west and bottom
    east corners.

    All positions use longitude and latitude coordinates.
    """
    claimed = False

    for location in Locations.objects.all():

        if ((posLat <= location.trCoOrd.latitude and posLat >= location.blCoOrd.latitude) and (posLong <= location.trCoOrd.longitude and posLong >= location.blCoOrd.longitude)):
            claimed = True
            break

    location.claimedBy = User.objects.get(pk=userID)
    location.save()

    return claimed
