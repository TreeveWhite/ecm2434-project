from django.contrib.auth.models import User
from exeterDomination.models import Locations


def posInRec(posLat : int, posLong : int) -> bool:
    """
    This function is used to check if a position is within a rectangle defined by its top west and bottom
    east corners.

    All positions use longitude and latitude coordinates.
    """
    inBuilding = None
    for location in Locations.objects.all():

        if ((posLat <= location. and posLat >= bottom) and (posLong <= west and posLong >= east)):
            inBuilding = location
    
    return inBuilding
