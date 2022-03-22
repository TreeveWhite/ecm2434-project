"""
alarms.py
=======================================
This file holds all the functions related to locations in articular when
handling the function which determins if a players longitude and lattude
are inside that of ay building in the system.
"""

from django.contrib.auth.models import User
from exeterDomination.models import Locations


def posInRec(userID: int, posLat: int, posLong: int) -> bool:
    """
    This function is used to check if a position is within a rectangle defined by its top
    west and bottom east corners.

    All positions use longitude and latitude coordinates.

    :param userID: The userID checking if in any buildings.
    :type userID: int
    :param posLat: The latitude of the user's location.
    :type posLat: float
    :param posLong: The longitude of the user's location.
    :type posLong: float

    :return: The name of the location claimed (if one is claimed).
    :rtype: str
    """
    claimed = False

    # Compares users long and lat to every building in system.
    for location in Locations.objects.all():

        print(location.name)
        print("Player Lat:", posLat)
        print("Player Long:", posLong)
        print(
            "Location Lat Top:",
            location.topRightCoordinate.latitude,
            " Location Lat Bottom: ",
            location.bottomLeftCoordinate.latitude)
        print(location.topRightCoordinate.latitude >=
              posLat >= location.bottomLeftCoordinate.latitude)

        print(
            "Location Long left:",
            location.bottomLeftCoordinate.longitude,
            " Location Long Right: ",
            location.topRightCoordinate.longitude)
        print(location.topRightCoordinate.longitude >=
              posLong >= location.bottomLeftCoordinate.longitude)
        print()

        if (location.topRightCoordinate.latitude >= posLat >= location.bottomLeftCoordinate.latitude) and (
            location.topRightCoordinate.longitude >= posLong >= location.bottomLeftCoordinate.longitude):
            # Users position is inside location
            location.claimedBy = User.objects.get(pk=userID)
            location.save()
            claimed = True

            break

    if not claimed:
        # The player is not inside any recognised building.
        return ""
    # The player has claimed a building.
    return location.name
    