from django.contrib.auth.models import User
from exeterDomination.models import Locations


def posInRec(userID: int, posLat: int, posLong: int) -> bool:
    """
    This function is used to check if a position is within a rectangle defined by its top west and bottom
    east corners.

    All positions use longitude and latitude coordinates.
    """
    claimed = False

    for location in Locations.objects.all():
        # print(location.name)
        # print("Player Lat:", posLat)
        # print("Player Long:", posLong)
        # print("Location Lat Top:", location.trCoOrd.latitude, " Location Lat Bottom: ", location.blCoOrd.latitude)
        # print(posLat <= location.trCoOrd.latitude and posLat >= location.blCoOrd.latitude)

        # print("Location Long left:", location.blCoOrd.longitude, " Location Long Right: ", location.trCoOrd.longitude)
        # print(posLong <= location.trCoOrd.longitude and posLong >= location.blCoOrd.longitude)
        # print()
        
        if ((posLat <= location.trCoOrd.latitude and posLat >= location.blCoOrd.latitude) and (posLong <= location.trCoOrd.longitude and posLong >= location.blCoOrd.longitude)):
            location.claimedBy = User.objects.get(pk=userID)
            location.save()
            claimed = True
        
            break

    if claimed == False:
        return ""
    else:
        return location.name
