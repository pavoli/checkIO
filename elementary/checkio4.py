# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def checkio(words):
    count = 0
    for i in words.split(' '):
        if i.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False


if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")