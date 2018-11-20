# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

#def popular_words(text: str, words: list) -> dict:
def popular_words(text, words):
    #new_text = [i.lower() for i in text.replace('\n',' ').split(' ') if i]
    #d = {a.lower():0 for a in words}
    #for k in d:
    #    for i in new_text:
    #        if k == i:
    #
    return {word:text.lower().split().count(word) for word in words}


#def popular_words(text):
#    for i in text.strip('\n').split(' '):
#        print i

if __name__ == '__main__':
    #popular_words('''\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n''')
    print (popular_words('''\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    })