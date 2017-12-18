# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
You are given a non-empty list of integers (X).
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]
"""

lst = [1, 2, 3, 1, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [5, 5, 5, 5, 5]
#lst = [10, 9, 10, 10, 9, 8]

#def checkio(lst):
#    work_list = lst[:]
#    result_list = []
#    for i in work_list:
#        if work_list.count(i)>1:
#            result_list.append(i)
#    return result_list

#def checkio(data):
#    return [i for i in data if data.count(i)>1]

def checkio(data):
    return list(filter(lambda i: data.count(i)>1, data))

if __name__ == '__main__':
    print(checkio(lst))