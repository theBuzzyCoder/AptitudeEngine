#!/usr/bin/python3

import formula as f

# class contains conversion methods for conversion for speeds

class Time:
    """ class contains conversion methods for speed """

    # constructor takes speed and its unit
    def __init__(self,hours,minutes,seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    #convert the time to seconds
    def to_secs(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    #convert time to hours
    def to_hours(self):
        return f.rd(self.__hours + self.__minutes / 60 + self.__seconds / 3600)

def units(unit):
    if unit == "m":
        return " seconds"
    else:
        return " hours"
