# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:07:40 2022

@author: knmoa
"""
import matplotlib.pyplot as plt

xcorA = int(input('X koordinat punkt A: '))
ycorA = int(input('Y koordinat punkt A: '))

xcorB = int(input('X koordinat punkt B: '))
ycorB = int(input('Y koordinat punkt B: '))

yplot = [ycorA, ycorB]
xplot = [xcorA, xcorB]

print(f'\nvektoren fra A ({xcorA}, {ycorA}) og B ({xcorB}, {ycorB}) er [{xcorB-xcorA}, {ycorB-ycorA}]')

plt.figure
plt.ylabel('Y-akse')
plt.xlabel('X-akse')
ax = plt.gca()
ax.annotate(f'A({xcorA},{ycorA})', (xcorA,ycorA),fontsize=10)
ax.annotate(f'B({xcorB},{ycorB})', (xcorB,ycorB),fontsize=10)
plt.plot(xcorA, ycorA, 'x')
plt.plot(xcorB, ycorB, 'x')
plt.grid()
plt.plot(xplot, yplot)
plt.show()