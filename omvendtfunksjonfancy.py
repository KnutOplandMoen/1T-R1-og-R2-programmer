# -*- coding: utf-8 -*-
"""
@author: knmoa

program som omhandler omvendte funksjoner

i programmet vil det plottes graf til vanlig og omvendt funksjon
videre blir det også plottet en speilingslinje mellom disse to på formen y = x
disse grafene vil kun bli plottet dersom funksjonen er en-entydig i definisjonmengden
til funksjonen, som er noe som blir sjekket i starten av programmet ved å se på 
stigningen til hver x verdi med ett intervall på 0.1 som kan endres for bedre nøyaktighet

"""
import matplotlib.pyplot as plt

#definerer funksjon
def f(x):
    return x**2

#spør om definisjonsmengde
xstart = float(input('start på definisjonsmengde til funksjon: '))
xslutt = float(input('ende på definisjonsmengde til funksjon: '))

#definerer liste til x og y verdier
xverdier = []
yverdier = []
#definerer variabler
funksjon = ''
delta_x = 0.1
x = xstart

#finner alle x og y verdier og legger dette i lister
while x <= xslutt+delta_x:
    y = f(x)
    xverdier.append(x)
    yverdier.append(y)
    x += delta_x
 
#definerer liste for den deriverte 
derivert = []
#legger til verdier i derivert listen 
for i in range(len(xverdier)-1):
    derivert.append((yverdier[i+1] - yverdier[i])/(xverdier[i+1]-xverdier[i]))

#sjekker om funksjonen vokser eller synker i definisjonsmengden
if yverdier[0] - yverdier[-1] < 0:
    funksjon = 'stigende'
elif yverdier[0] - yverdier[-1] > 0:
    funksjon = 'synkende'
else:
    funksjon = 'rett'

print(funksjon)

print(derivert)
#sjekker om funksjonen er strengt voksende eller avtagende
for i in range(len(derivert)-1):
    if funksjon == 'stigende':
        #sjekke om den deriverte bytter fortegn
        if derivert[i] < 0:
            funksjon = 'ikke strengt voksende'
            print('\nikke strengt voksende')
            break
    elif funksjon == 'synkende':
        #sjekke om den deriverte bytter fortegn
        if derivert[i] > 0:
            funksjon = 'ikke strengt avtagende'
            print('\nikke strengt avtagende')
            break
        
if funksjon != 'stigende' and funksjon != 'synkende':
    print('\nfunksjon var ikke en-entydig, plotter ikke grafer')
    
else:
    print('\nfunksjon er en-entydig, plotter grafer')
      
    #definerer verdier for den omvendte funksjonen
    xverdier = xverdier[:-1]
    yverdier = yverdier[:-1]
    xomvendt = yverdier
    yomvendt = xverdier
    
    #definerer liste for speilingslinjen
    linjerx = []
    linjery = []

    #legger til verdier i liste for speilingslinje
    for i in range(xverdier[0], int(round(max(yverdier), 0))):
        linjerx.append(i)
        linjery.append(i)
    
    print(f'\ndefinisjonsmengde til vanlig funksjon: [{xstart},{xslutt}]')
    print(f'verdimengde til vanlig funksjon: [{f(xstart)},{f(xslutt)}]')
    
    print(f'\ndefinisjonsmengde til omvendt funksjon: [{f(xstart)},{f(xslutt)}]')
    print(f'verdimengde til omvendt funksjon: [{xstart},{xslutt}]')
    
    #plotter grafer
    plt.plot(xverdier, yverdier, 'darkgreen', label = 'funksjon')
    plt.plot(xomvendt, yomvendt, 'darkblue', label = 'omvendt funksjon')
    plt.plot(linjerx, linjery,'red', label = 'linje')
    plt.grid()
    plt.show