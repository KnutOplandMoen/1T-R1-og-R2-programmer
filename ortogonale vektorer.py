# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:34:36 2023

@author: knmoa
"""

x1 = 0
y1 = 0
z1 = 0

x2 = 3
y2 = 2
z2 = 9

v1 = [x1, y1, z1]
v2 = [x2, y2, z2]

def skalar(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

skalar = skalar(v1, v2)
if skalar == 0:
    print('vektorer ortogonale')
    
elif skalar > 0:
    print('vektorer med spiss vinkel mellom seg')

elif skalar < 0:
    print('vektorer med stump vinkel mellom seg')



