"""
Common functions for Advent of Code 2019

I think intcode is gonna get expanded some day so it will be added into
this file when it does

@author: DoraMemo
"""

def parseFile(filename):
    content = [x.strip() for x in open(filename).readlines()]
    return content

def parseIntcode(filename):
    f = open(filename)
    line = f.readline()
    f.close()
    
    program = line.split(",")
    program = [int(x) for x in program]
    return program