# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def index_power(array, n):
    try:
        return pow(array[n], n)
    except:
        return -1
    #return array[n] ** n if len(array) > n else -1



if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9
    assert index_power([1, 3, 10, 100], 3) == 1000000
    assert index_power([0, 1], 0) == 1
    assert index_power([1, 2], 3) == -1