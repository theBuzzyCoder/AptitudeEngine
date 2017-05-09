#!/usr/bin/python3

import formula as f

# class contains conversion methods for conversion for speeds

class Speed:
    """ class contains conversion methods for conversion for speeds """

    # constructor takes speed and its unit
    def __init__(self,speed,unit):
        self.__speed = speed
        self.__unit = unit

    # converts the speed to meters
    def to_mtrps(self):
        if self.__unit == "m":
            return self.__speed
        elif self.__unit == "k":
            return f.rd(self.__speed * 5 / 18)
        else :
            return f.rd( 1.61 * self.__speed * 5 / 18)

    # converts the speed to kilometers
    def to_kmph(self):
        if self.__unit == "m":
            return f.rd(self.__speed * 3.6)
        elif self.__unit == "k":
            return self.__speed
        else :
            return f.rd(1.61 * self.__speed)

    # converts speed to miles
    def to_miph(self):
        if self.__unit == "m":
            return f.rd(self.__speed * 3.6 * 0.62)
        elif self.__unit == "k":
            return f.rd(self.__speed * 0.62)
        else :
            return self.__speed
            
def units(unit):
    if unit == "m":
        return " meters per second"
    elif unit == "k":
        return " kilometers per hour"
    else:
        return " miles per hour"
