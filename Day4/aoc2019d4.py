# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 02:16:55 2019

@author: DoraMemo
"""

import math

lower = 264793
upper = 803935
valid = 0

while lower <= upper:
    lowerstr = str(lower)
    
    repeatedDigits = {}
    pairDigits = 0
    neverDecreaseDigits = 1
    
    for i in range(0, 5):
        # Two adjacent digits are the same
        if (lowerstr[i] == lowerstr[i+1]):
            if (lowerstr[i] not in repeatedDigits.keys()):
                repeatedDigits[lowerstr[i]] = 1
            else:
                repeatedDigits[lowerstr[i]] += 1
        
        # the digits never decrease
        if (int(lowerstr[i]) > int(lowerstr[i+1])):
            neverDecreaseDigits = 0
            break
    
    for val in repeatedDigits.values():
        if (val == 1):
            pairDigits = 1
    
    # combined
    if (pairDigits and neverDecreaseDigits):
        valid += 1
        print(lower, "is valid")
    
#    if (adjSameDigit or neverDecreaseDigits):
#        print(lower, adjSameDigit, neverDecreaseDigits)
    
    lower += 1
    
print(valid)