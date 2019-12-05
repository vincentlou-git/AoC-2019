# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 02:16:55 2019

@author: DoraMemo
"""

import math

def intcode(nums):
    """
    nums: list of numbers
    """
    
    for i in range(0, len(nums), 4):
        if (nums[i] == 1):
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
        elif (nums[i] == 2):
            nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
        elif (nums[i] == 99):
            return nums[0]
        else:
            print("Unknown opcode", nums[i], "at pos", i);
            return nums[0]
            
    return nums[0]

f = open("input.txt")
line = f.readline()
f.close()

program = line.split(",")
program = [int(x) for x in program]
control = program

total = 0
while (1):
    program = [x for x in control]
    total += 1
    print("Attempt",total)
    verb = total % 100
    noun = math.floor(total / 100)
    program[1] = noun
    program[2] = verb
    
    if (intcode(program) == 19690720):
        print("Answer", total)
        break
    
    if (verb >= 99 and noun >= 99):
        print("Reached end of bruteforce. Terminating")
        break