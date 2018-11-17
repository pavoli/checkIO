# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

def popular_words(text: str, words: list) -> dict:
    d = {a.lower():0 for a in words}
    new_text = [i.strip('\n').lower() for i in text.split(' ') if i]

    for k, v in d.items():
        for i in new_text:
            if k == i:
                d[k] =+ 1

    for i in d:
        print(d)

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