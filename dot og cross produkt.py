# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:39:58 2023

@author: knmoa
"""

import pylab as vha
v = vha.array([6, 0, 2])
u = vha.array([5, 1, 3])
w = vha.array([0, 4, 6])

grunnflate = vha.cross(v, u)

grunnflateareal = vha.sqrt((grunnflate[0]**2)+(grunnflate[1]**2)+(grunnflate[2]**2))

volum = vha.dot(grunnflate, w)

print(abs(volum))
print(grunnflateareal)

