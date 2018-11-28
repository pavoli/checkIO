# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def left_join(phrases):
    return ((','.join(phrases).replace('right', 'left')))


if __name__ == '__main__':
    left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    left_join(("bright aright", "ok")) == "bleft aleft,ok"
    left_join(("brightness wright",)) == "bleftness wleft"
    left_join(("enough", "jokes")) == "enough,jokes"
    #assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    #assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    #assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    #assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")