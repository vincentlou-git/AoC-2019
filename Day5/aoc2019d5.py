# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 02:06:37 2019

@author: DoraMemo
"""

def valParamMode(mode, val, nums):
    if (mode == 0): # location
        return nums[val]
    elif (mode == 1): # value
        return val
    else:
        print("unknown mode", mode)
    
    return -1

def intcode(nums):
    """
    nums: list of numbers
    """
    
    # opcode: num_params
    paramCount = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            99: 0
            }
    
    ip = 0 # instruction pointer
    while ip < len(nums):
        print("ip at",ip,nums[ip])
        opcode = nums[ip] % 100
        nParams = paramCount[opcode]
        inststr = str(nums[ip])
        paramMode = [] if len(inststr) <= 2 else [int(inststr[i]) for i in range(len(inststr)-3, -1, -1)]
        # fill the remaining zeros
        paramMode = [(paramMode[i] if i < len(paramMode) else 0) for i in range(nParams)]
        
        a = 0 ; b = 0 ; c = 0
        if (nParams >= 3):
            c = valParamMode(paramMode[2], nums[ip+3], nums)
        if (nParams >= 2):
            b = valParamMode(paramMode[1], nums[ip+2], nums)
        if (nParams >= 1):
            a = valParamMode(paramMode[0], nums[ip+1], nums)
        
#        print("Inststr =", inststr)
#        print("ParamMode =", paramMode)
        
        if (opcode == 1): # add(a, b, store_pos)
            nums[nums[ip+3]] = a + b
#            print(nums[ip+3], "=", a, "+", b)
        elif (opcode == 2): # mult(a, b, store_pos)
            nums[nums[ip+3]] = a * b
#            print(nums[ip+3], "=", a, "x", b)
        elif (opcode == 3): # take input, store in (n)
            print("Pls input")
            nums[nums[ip+1]] = int(input())
        elif (opcode == 4): # output / print out parameter (n)
            print(nums[nums[ip+1]])
        elif (opcode == 5): # JIT(a > 0, ip = b)
            if (a > 0):
                ip = b
                continue
        elif (opcode == 6): # JIF(a == 0, ip = b)
            if (a == 0):
                ip = b
                continue
        elif (opcode == 7): # less(a < b, store_pos = 1 : 0)
            nums[nums[ip+3]] = 1 if (a < b) else 0
        elif (opcode == 8): # equals(a == b, store_pos = 1 : 0)
            nums[nums[ip+3]] = 1 if (a == b) else 0
        elif (opcode == 99):
            return 1 # finished successfully
        else:
            print("Unknown instruction", nums[ip], "at pos", ip)
            print("Opcode =", opcode)
            print("Inststr =", inststr)
            print("ParamMode =", paramMode)
            return nums[0]
        
        ip += nParams + 1
            
    return nums[0]

f = open("input.txt")
line = f.readline()
f.close()

program = line.split(",")
program = [int(x) for x in program]

print(program)

intcode(program)