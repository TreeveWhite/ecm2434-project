


def posInRec(top : int, west : int, bottom : int, east : int, posLat : int, posLong : int) -> bool:
    """
    This function is used to check if a position is within a rectangle defined by its top west and bottom
    east corners.

    All positions use longitude and latitude coordinates.
    """
    inArea = False

    if ((posLat <= top and posLat >= bottom) and (posLong <= west and posLong >= east)):
        inArea = True
    
    return inArea
