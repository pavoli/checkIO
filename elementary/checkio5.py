# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def checkio(number):
    return (eval('*'.join([i for i in str(number) if int(i)>0])))


if __name__ == '__main__':
    checkio(123405) == 120
    checkio(999) == 729
    checkio(1000) == 1
    checkio(1111) == 1