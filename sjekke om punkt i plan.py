# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:18:31 2023

@author: knmoa
"""

punkt = [0, 1, 0]
vektor = [5, 1, 2]
punkt2 = [0, 1, 0]

d = punkt[0]*vektor[0]+punkt[1]*vektor[1]+punkt[2]*vektor[2]

def funksjon(punkt, vektor, d):
    return punkt[0]*vektor[0]+punkt[1]*vektor[1]+punkt[2]*vektor[2] - d

if funksjon(punkt2, vektor, d) == 0:
    print('punkt', punkt2, 'i planet')
else:
    print('punkt', punkt2, 'ikke i planet')