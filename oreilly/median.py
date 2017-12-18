# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
A median is a numerical value separating the upper half of a sorted array of numbers from the lower half.
In a list where there are an odd number of entities,
the median is the number found in the middle of the array.
If the array contains an even number of entities,
then there is no single middle value,
instead the median becomes the average of the two numbers found in the middle.
For this mission, you are given a non-empty array of natural numbers (X).
With it, you must separate the upper half of the numbers from the lower half and find the median.
Input: An array as a list of integers.
Output: The median as a float or an integer.
"""

#str = [1, 2, 3, 4, 5]
#str = [3, 1, 2, 5, 3]
#str = [1, 300, 2, 200, 1]
str = [3, 6, 20, 99, 10, 15]


def checkio(str):
    new_str = sorted(str[:])
    idx = int((len(new_str)-1)/2)
    median = 0
    if len(new_str)%2 == 0:
        median = (new_str[idx] + new_str[idx+1]) / 2
    else:
        median = new_str[idx]
    return median


if __name__ == '__main__':
    #checkio(str)
    assert checkio([1, 2, 3, 4, 5]) == 3
    assert checkio([3, 1, 2, 5, 3]) == 3
    assert checkio([1, 300, 2, 200, 1]) == 2
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5