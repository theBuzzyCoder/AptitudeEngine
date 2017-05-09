#!/usr/bin/python3

import formula as f

# class contains conversion methods for conversion of distances

class Distance:
    """class contains conversion methods for distance"""

    # constructor takes distance and its unit
    def __init__(self,distance,unit):
        self.__distance = distance
        self.__unit = unit

    # converts the distance to meters
    def to_mtr(self):
        if self.__unit == "m":
            return self.__distance
        elif self.__unit == "k":
            return self.__distance * 1000
        else :
            return f.rd(1.61 * self.__distance * 1000)

    # converts the distance to kilometers
    def to_km(self):
        if self.__unit == "m":
            return f.rd(self.__distance/1000)
        elif self.__unit == "k":
            return self.__distance
        else :
            return f.rd(1.61 * self.__distance)

    # converts distance to miles
    def to_mi(self):
        if self.__unit == "m":
            return f.rd(self.__distance/1000 * 0.62)
        elif self.__unit == "k":
            return f.rd(self.__distance * 0.62)
        else :
            return self.__distance

def units(unit):
    if unit == "m":
        return " meters"
    elif unit == "k":
        return " kilometers"
    else:
        return " miles"
