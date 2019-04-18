# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def sun_angle(time):
    h, m = time.split(':')
    h = int(h)
    m = int(m)

    if h < 6 or (h >= 18 and m > 0):
        print("I don't see the sun!")
        return "I don't see the sun!"
    else:
        print((h-6)*15 + m * 0.25)
        return ((h-6)*15 + m * 0.25)


if __name__ == '__main__':
    sun_angle("07:00") == 15
    sun_angle("12:15") == 93.75
    #sun_angle("01:23") == "I don't see the sun!"
    print(sun_angle("01:23"))