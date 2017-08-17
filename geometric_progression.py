# -*- coding: utf-8 -*-
'''
Python Version: Python3.6
Authored by: Akshay Kumar
Edited by: theBuzzyCoder
Last Edited on: Aug 17, 2017

Contains the geometric progression function
'''


def geometric_progession(series, index):
    '''
    Calculates Geometric Progression based on the series and index.
    series is a list of integers
    index is the nth item
    '''
    # a = first term, r = common ratio
    first_term = series[0]
    ratio = series[1] / series[0]
    nth_item = first_term * ratio ** (index - 1)
    return nth_item


if __name__ == '__main__':
    ITEM_LIST = [2, 6, 18]
    POSITION = 4
    print("nth item = ", geometric_progession(ITEM_LIST, POSITION))
