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
      1. Overhead of suspensions for large data set
   
Optimizations:
1. Store the number of orbits of a [name] once computed.
   Then later on if that [name]'s # of orbits is requested,
   return that value from a lookup table;
   otherwise, compute
NOTE: I guess that lookup table idea wouldn't work because you never know
      when is the parent name terminated
"""

nameOrbitsDict = {}

def numOrbits(child, checkedParents):    
    i = 0
    count = 0
#    print(checkedParents)
    while (i != len(relationships)):
        r = relationships[i]
#        print("Checking", r, "in child =", child)
        if (r[1] == child and r[0] not in checkedParents):
#            print("Found a parent in", r)
            checkedParents.add(r[0])
            parentCount = nameOrbitsDict[r[0]] if r[0] in nameOrbitsDict.keys() \
                          else numOrbits(r[0], checkedParents)
            count += 1 + parentCount
#            print("Count is now", count, "for", child)
            return count # 1 (direct) + parent orbits
        i += 1
#    print(child, "has", count, "orbits")
    nameOrbitsDict[child] = count
    return count

def minOrbitTransfers(orbit1, orbit2):
    """
    Logic draft:
        Backtracking
        Find parent chain for orbit1, store in stack1
        Find parent chain for orbit2, store in stack2
        end root (parent) / top of stack should be the same
        pop stack1 until the popped element is no longer in stack2
        then the parent of the popped element is the branching planet
        pop stack2 until the popped element == branching planet
        then join the two stacks, remember to remove orbit1 and orbit2
    """
    return

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

relationships = splitOrbits("input.txt")
nameSet = allNames(relationships)
print(nameSet)
# Print this for part 1
print(sum(numOrbits(x, set()) for x in nameSet))

# Print this for part 2
#print(minOrbitTransfers("YOU", "SAN"))