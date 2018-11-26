# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def find_message(text):
    return ''.join([x for x in text if x.istitle()])


if __name__ == '__main__':
    find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"