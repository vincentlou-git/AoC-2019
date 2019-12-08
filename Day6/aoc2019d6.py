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
(The following is only my thought process. Please do not take them as a
perfect description of what the functions do.)

Keep a map of orbits.
Feed in a [name] in function, return:
1. direct orbits (whether this [name] has a [foo])[name] entry
   can also just keep a list of direct orbits (right side) when reading data
   have a list or all [name]s. Have a **map** of whether this [name] has a direct orbit
2. indirect orbits, oh boy
   recursion might help here
   enter [name], feed the "parent" of this [name] in function, +1 each time.
   if "parent" doesn't have a super-parent, terminate (base case)
NOTE: Recursion actually wouldn't work well...
      1. Overhead for copying truncated list
      2. 
   
Optimizations:
1. Store the number of orbits of a [name] once computed.
   Then later on if that [name]'s # of orbits is requested,
   return that value from a lookup table;
   otherwise, compute
NOTE: I guess that lookup table idea wouldn't work because you never know
      when is the parent name terminated
"""

def numOrbits(child, checkedParents, relationships):
    """
    INPUT:
        name    child name
        relIndex   index of relationship we're checking
        parents, children needed
    """
    
    i = 0
    count = 0
    print(checkedParents)
    while (i != len(relationships)):
        r = relationships[i]
        print("Checking", r, "in child =", child)
        if (r[1] == child and r[0] not in checkedParents):
            print("Found a parent in", r)
#            del relationships[i]
            checkedParents.add(r[0])
            count += 1 + numOrbits(r[0], checkedParents, relationships)
            print("Count is now", count, "for", child)
            return count # 1 (direct) + parent orbits
        i += 1
    print(child, "has", count, "orbits")
    return count

def splitOrbits(filename):
    content = [x.strip().split(")") for x in open(filename).readlines()]
    return content

def allNames(relationships):
    nameSet = []
    for r in relationships:
        if (r[0] not in nameSet):
            nameSet.append(r[0])
        if (r[1] not in nameSet):
            nameSet.append(r[1])
    return nameSet

rels = splitOrbits("input_test.txt")
nameSet = allNames(rels)
print(nameSet)
print(sum(numOrbits(x, set(), rels) for x in nameSet))