# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:34:28 2022

@author: knmoa
"""
import pandas as pd
import matplotlib.pyplot as plt

#Laster inn datasettet

fil = pd.read_csv("bakterietetthet.csv", sep=";", comment="#", decimal=".")

tid = fil["Tid"].tolist()
tetthet = fil["Tetthet"].tolist()

plt.plot(tid, tetthet, "x")

xstart=tid[0]
xslutt=tid[-1]
ystart=tetthet[0]
delta_x = 0.1
k = 0.06
B = 1
print('hei')
xverdier = []
yverdier = []

x = xstart
y = ystart
print('hei')
while x <= xslutt:
    xverdier.append(x)
    yverdier.append(y)
    x = x + delta_x
    y = y + delta_x*k*y*(1-y/B)

plt.plot(xverdier, yverdier)
plt.grid()
plt.show()
