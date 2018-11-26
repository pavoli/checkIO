# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def checkio(array):
    return sum([y for x, y in enumerate(array) if x % 2 == 0])*array[-1] if array else 0
    #return sum(array[::2]) * array[-1] if array else 0


if __name__ == '__main__':
    #checkio([0,1,2,3,4,5])
    #checkio([1, 3, 5])
    #print(checkio([6]))
    #print(checkio([]))
    print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]))