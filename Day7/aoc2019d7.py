# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 03:03:30 2019

@author: DoraMemo
"""

import sys
sys.path.append('..')
from commonfunctions import *
from intcode import *

program = parseIntcode("input.txt")
print(program)

intcode(program)