# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


from collections import Counter

def frequency_sort(items):
    #return (sorted(items, key=lambda x: (items.count(x), x), reverse=True))
    print (sorted(items, key=lambda x: (items.count(x), x)))


if __name__ == '__main__':
    #frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
    frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
    #frequency_sort([17, 99, 42]) == [17, 99, 42]
    #frequency_sort([]) == []
    #frequency_sort([1]) == [1]
    #frequency_sort([1, 2, 2, 1]) == [1, 1, 2, 2]