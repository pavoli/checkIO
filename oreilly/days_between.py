# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
You are given two dates as tuples with three numbers - year, month and day.
For example: 19 April 1982 will be (1982, 4, 19).
You should find the difference in days between the given dates.
For example between today and tomorrow = 1 day.
The difference will always be either a positive number or zero, so don't forget about absolute value.
Input: Two dates as tuples of integers.
Output: The difference between the dates in days as an integer.
"""

from datetime import date

def days_diff(t1, t2):
    return abs(date(*t1)-date(*t2)).days

if __name__ == '__main__':
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238