# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def translate(words):
    new_words = words.split(' ')
    print(len(new_words))
    answer = ''
    for x in new_words:
        print(x)
        answer += x
        if x in 'aeiouy':
            gap = 3
        else:
            gap = 2
        print('gap={}'.format(gap))
        new_words = new_words[2:]
        print('new_words={}'.format(new_words))
    print(answer)

if __name__ == '__main__':
    #translate("hieeelalaooo") == "hello"
    translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    #translate("aaa bo cy da eee fe") == "a b c d e f"
    #translate("sooooso aaaaaaaaa") == "sos aaa"