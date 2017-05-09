#!/usr/bin/python3
def arithmetic_progression(series, index):
    '''
    Author:Ankit Bhagat
    Last Updated: Jan 22, 2017
    series is list of integers
    index is the term we have to find
    '''
    a = series[0]
    # a is first term of series
    d = series[1] - series[0]
    # d is common diffrence
    an = a + (index - 1) * d
    return an
