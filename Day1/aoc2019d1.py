# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 02:16:55 2019

@author: DoraMemo
"""

import math

def part2fuel(mass):
    if (mass <= 6):
        return 0
    
    fuel = math.floor(mass/3)-2
    return fuel + part2fuel(fuel)



with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
content = [int(x) for x in content]

total = 0
for mass in content:
    total += part2fuel(mass)
    
print(total)