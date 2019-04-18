# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def time_converter(str):
    h, m = str.split(':')
    h = int(h)
    midday = ''
    if h > 11:
        midday = 'p.m.'
    else:
        midday = 'a.m.'

    if h == 0:
        h = 12
    if h > 12:
        h = int(h)%12

    #return ('{}:{} {}'.format(h, m, midday))
    print ('{}:{} {}'.format(h, m, midday))


if __name__ == '__main__':
    time_converter('12:30') == '12:30 p.m.'
    time_converter('09:00') == '9:00 a.m.'
    time_converter('23:15') == '11:15 p.m.'
    time_converter('00:00') == '12:00 a.m.'