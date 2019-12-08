# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:49:01 2019

@author: DoraMemo
"""

import sys
sys.path.append('..')
from commonfunctions import *

# direct orbits
# indirect orbits

"""
Keep a map of orbits.
Feed in a [name] in function, return:
1. direct orbits (whether this [name] has a [foo])[name] entry
   can also just keep a list of direct orbits (right side) when reading data
   have a list or all [name]s. Have a **map** of whether this [name] has a direct orbit
2. indirect orbits, oh boy
   recursion might help here
   enter [name], feed the "parent" of this [name] in function, +1 each time.
   if "parent" doesn't have a super-parent, terminate (base case)
   
Optimizations:
1. Store the number of orbits of a [name] once computed.
   Then later on if that [name]'s # of orbits is requested,
   return that value from a lookup table;
   otherwise, compute
"""

def orbits(name, m):
    return 1

content = parseFile("input.txt")