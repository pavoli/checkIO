# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def best_stock(data):
    max_stock = dict([data.popitem()])
    for k, v in  data.items():
        if v > list(max_stock.values())[0]:
            max_stock.clear()
            max_stock = {k:v}
    return list(max_stock.keys())[0]


"""
def best_stock(data):
    return sorted(data.items(), key=lambda x: -x[1])[0][0]
"""
"""
def best_stock(data):
    return sorted(data.items(), key=lambda x: x[1], reverse=True)[0][0]
"""
"""
best_stock = lambda d: max(d, key=d.get)
"""
"""
def best_stock(data):
   return max(data,key=data.get)
"""


if __name__ == '__main__':
    """
    best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    })# == 'ATX'
    """
    best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI'