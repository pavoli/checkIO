# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

def popular_words(text: str, words: list) -> dict:
    for i in text.split(' '):
        print(i)


if __name__ == '__main__':
    popular_words('''
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    ''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }