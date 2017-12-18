# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
Input: A password as a string (Unicode for python 2.7).
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
In the results you will see the converted results.
"""

#str = 'A1213pokl'
#str = 'bAse730onE'
#str = 'asasasasasasasaas'
#str = 'QWERTYqwerty'
#str = '123456123456'
#str = 'QwErTy911poqqqq'
str = 'ULFFunH8ni'

def checkio(str):
    if len(str) < 10:
        return False
    digit = 0
    lower_str = 0
    upper_str = 0
    for i in str:
        if i.isdigit():
            digit += 1
        if i.islower():
            lower_str += 1
        if i.isupper():
            upper_str += 1
    print('digit= ', digit, '| lower=', lower_str, '| upper=', upper_str)
    if digit >= 1 and lower_str >= 1 and upper_str >= 1:
        return True
    else:
        return False

"""
def checkio(data):
    if len(data) < 10: return False
    islower = isupper = isdigit = False
    for c in data:
        if "a" <= c <= "z": islower = True
        if "A" <= c <= "Z": isupper = True
        if "0" <= c <= "9": isdigit = True
    return islower and isupper and isdigit
"""

"""
checkio = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    ) 
"""

"""
import re
def checkio(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 10 else False
"""

if __name__ == '__main__':
    print(checkio(str))