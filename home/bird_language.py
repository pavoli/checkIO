# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def translate(words):
    new_words = words.split(' ')
    answer = ''
    for x in new_words:
        print(x)

if __name__ == '__main__':
    #translate("hieeelalaooo") == "hello"
    translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    #translate("aaa bo cy da eee fe") == "a b c d e f"
    #translate("sooooso aaaaaaaaa") == "sos aaa"