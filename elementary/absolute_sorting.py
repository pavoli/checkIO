# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def checkio(elements):
    #print(sorted(elements, key=lambda x: abs(x)))
    print(sorted(elements, key=abs))


if __name__ == '__main__':
    print(checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20])  # or (-5, 10, 15, -20)
    print(checkio((1, 2, 3, 0)) == [0, 1, 2, 3])
    print(checkio((-1, -2, -3, 0)) == [0, -1, -2, -3])