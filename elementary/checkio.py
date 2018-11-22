# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)



if __name__ == '__main__':
    checkio(15) == "Fizz Buzz"
    #checkio(6) == "Fizz"
    #checkio(5) == "Buzz"
    #checkio(7) == "7"