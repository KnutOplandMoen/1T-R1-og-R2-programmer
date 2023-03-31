# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:59:09 2023

@author: knmoa
"""
import math 
antall = 0
for x in range(-3, 4):
    for y in range(-3, 4):
        for z in range(-3, 4):
            if math.sqrt(x**2+y**2+z**2) == 3:
                antall += 1

print(antall)
                
            