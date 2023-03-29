# -*- coding: utf-8 -*-
"""
@author: knmoa

Program for å finne k verdi som en funksjon må ha
for å treffe y = ykoordinat i punktet x = xkoordinat

programmet har en visuell del ved at det plottes graf 
til funksjon etter ønsket k verdi er funnet

programmet finner derimot kunn en tilnærmet verdi, med ønsket 
nøyaktighet som gis av variabelen 'nøyaktighet'

programmet kan utvides med mer nøyaktighet ved å sette en lavere 
verdi på nøyaktighets variablen, men også ved å legge til flere 
sjekkpunkter. dette vil derimot kreve mer maskinkraft...

"""

import matplotlib.pyplot as plt

#ønsket x koordinat og y koordinat der funksjonen skal gå igjennom 
xkoordinat = 20
ykoordinat = 90
#nøyaktighet, deltax og deltak
nøyaktighet = 0.5
deltax = 0.001
deltak = 0.0001
#definerer definisjonsmengde til funksjon
xstart = 0
xslutt = 30
#definerer f(xstart) ved variabel ystart
ystart = 10

#k start verdi og B konstant verdi
k = 0.0
B = 100

x = xstart 
y = ystart
#lager variabel for svar som brukes senere i while loopen
svar = 0

while svar > ykoordinat + nøyaktighet or svar < ykoordinat - nøyaktighet:
    k += deltak
    x = xstart
    y = ystart
    while x <= xslutt:
        y = y + deltax * k * y * (1 - y/B)
        x = x + deltax
        if x < xkoordinat + nøyaktighet and x > xkoordinat - nøyaktighet:
            svar = y
            break
    print(f'svar med k-verdi: {k} = {svar}')
    if svar > ykoordinat - nøyaktighet and svar < ykoordinat + nøyaktighet:
        break
    
#printer funnet k verdi    
print(f'k verdi: {k}') 

#setter x og y verdier tilbake til der de startet  
x = xstart
y = ystart
#lager lister for plotting av graf
xverdier = []
yverdier = []

#while loop for å legge til verdier i y og x lister
while x <= xslutt:
    xverdier.append(x)
    yverdier.append(y)
    y = y + deltax * k * y * (1 - y/B)
    x = x + deltax

#plotter grafer
plt.plot(xverdier, yverdier, 'green', label = 'f(x)')
plt.grid()
plt.plot([20], [90], 'x')
plt.show

