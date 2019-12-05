# -*- coding: utf-8 -*-
"""
Advent of Code 2019 Day3

@author: DoraMemo
"""

import math

def dir2cords(dirs):
    """
    dirs: a list of raw direction inputs
    
    OUTPUT:
        cords:  a list of coordinates representing the vertices of each line
    """
    cords = [[0,0] for x in range(len(dirs)+1)]
    
    # cords[0] should be [0, 0]
    
    for i in range(1, len(dirs)+1):
        d = dirs[i-1][0]
        val = int(dirs[i-1][1:])
        
        cords[i][0] = cords[i-1][0]
        cords[i][1] = cords[i-1][1]
        
        # x / horixontal. Right = (+)
        if (d == "L"):
            cords[i][0] -= val
        elif (d == "R"):
            cords[i][0] += val
        # y / vertical. Up = (+)
        elif (d == "U"):
            cords[i][1] += val
        elif (d == "D"):
            cords[i][1] -= val
        else:
            print("Invalid direction, skipping this instruction");
    
    return cords

def intersections(c1, c2):
    """c
    INPUT:
        c1, c2:         two lists of coordinates, 
                        representing a bunch of line segments
    OUTPUT:
        intersections:  a list of unique coordinates where the two lists of
                        line segments intersect
    """
    
    intersections = []
    
    # Horizontal:   x varies. (x1, y) (x2, y)
    # Vertical:     y varies. (x, y1) (x, y2)
    # Intersection: (x, y) - the constant values
    #                        only valid if x in [x1, x2]
    #                                  and y in [y1, y2]
    
    for i in range(len(c1)-1):        
        for j in range((i+1) % 2, len(c2)-1, 2):            
            # only check if two lines have different directions
            if (i % 2 == 1):
                # from c1
                x1 = min(c1[i][0], c1[i+1][0])
                x2 = max(c1[i][0], c1[i+1][0])
                y  = c1[i][1]
                 
                # from c2
                x  = c2[j][0]
                y1 = min(c2[j][1], c2[j+1][1])
                y2 = max(c2[j][1], c2[j+1][1])
                
                # check in range
                if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
                    intersections.append([x,y])
            
            else:
                # from c2
                x1 = min(c2[i][0], c2[i+1][0])
                x2 = max(c2[i][0], c2[i+1][0])
                y  = c2[i][1]
                 
                # from c1
                x  = c1[j][0]
                y1 = min(c1[j][1], c1[j+1][1])
                y2 = max(c1[j][1], c1[j+1][1])
                
                # check in range
                if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
                    intersections.append([x,y])
                    
    return intersections

def pointIsInLine(target, p1, p2):    
    minX = min(p1[0], p2[0])
    minY = min(p1[1], p2[1])
    maxX = max(p1[0], p2[0])
    maxY = max(p1[1], p2[1])
    return target[0] >= minX and target[0] <= maxX and target[1] >= minY and target[1] <= maxY

def steps(path, points):
    """
    INPUT:
        path:   following this path to find intersections.
                a list of coordinates [x,y].
        points: a list of points to reach (coordinates [x,y])
    OUTPUT:
        int_steps: a list of integers telling how many steps would
                   it take to follow path to reach each point in points
    """
    
    int_steps = [0 for i in range(len(points))]
    found = [0 for i in range(len(points))]
    
    for i in range(len(path)-1):
        p1 = path[i]
        p2 = path[i+1]
        
        for j in range(len(points)):
            if (found[j]):
                continue
                
            target = points[j]
            
            if (not pointIsInLine(target, p1, p2)):
                int_steps[j] += manhattan(p1, p2)
            else:
                int_steps[j] += manhattan(p1, target)
                found[j] = 1
    return int_steps

def manhattan(p1, p2):
    """
    point: [x,y]
    returns the manhattan distance from point to origin
    """
    
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

f = open("input.txt")
ln1 = f.readline()
ln2 = f.readline()
f.close()

cords1 = dir2cords(ln1.split(","))
cords2 = dir2cords(ln2.split(","))

#print(cords1)
#print(cords2)

ints = intersections(cords1, cords2)
dists = []

print("ints", ints)

for i in ints:
    dists.append(manhattan(i, [0,0]))
    
print("shortest md is", min(dists))

wire1steps = steps(cords1, ints)
wire2steps = steps(cords2, ints)

print("w1s", wire1steps)
print("w2s", wire2steps)

combined = []

for p in range(len(ints)):
    combined.append(wire1steps[p] + wire2steps[p])
    
print("combined", combined)
print("combined min", min(combined))