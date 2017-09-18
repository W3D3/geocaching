#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# GC29MX2 - Automobile 2
# Status: SOLVED

def getValue(name):
    total = 0
    for char in name.lower():
        if(char != ' '):
            total += ord(char) - 96
    return total


import webbrowser
import urllib
import sys

a = getValue('Lamborghini')   # goldenes Siegel (Lamborghini oder Porsche)
b = getValue('Volvo')      # Rundschild mit Speer (maybe VOLVO?)            ???
c = getValue('Subaru')    # Plejaden
d = getValue('Plymouth')     # Segelboot (nicht in der EU; westlich der Alpen)
e = getValue('Buick')     # drei Langschilder
f = getValue('Skoda')     # geflügelter Pfeil
g = getValue('Lancia')    # Fahnenmast
h = getValue('Wiesmann')  # Gecko
i = getValue('Maserati')  # Dreizack
j = getValue('Oldsmobile')  # Rakete (Daihatsu?)
k = getValue('Corvette')  # Ziel

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

# N 46° (B+C-D-1) , (A+C-D+E+F+I+K+4)
# E013° (E-F-G+H+I-J+13) , (A+B+C+D+E+F+G+H+J+34)

# (  B + C - D - 1)
n1 = b + c - d - 1
#(   A + C - D + E + F + I + K + 4)
n2 = a + c - d + e + f + i + k + 4
coord_n = 'N 46° ' + str(n1) + '.' + str(n2)

#   (E - F - G + H + I - J + 13)
e1 = e - f - g + h + i - j + 13
#   (A + B + C + D + E + F + G + H + J +34)
e2 = a + b + c + d + e + f + g + h + j + 34
coord_e = 'E013° ' + str(e1) + '.' + str(e2)


print coord_n, coord_e
if n1 > 60:
    sys.exit("Latitude is invalid.")
if e1 > 60:
    sys.exit("Longitude is invalid.")

if n1 > 40:
    sys.exit("Above Villach :()")
if n1 < 20:
    sys.exit("Below Villach")

controller = webbrowser.get('safari')
url = 'https://www.google.at/maps/search/' + \
    urllib.quote_plus(coord_n + ' ') + urllib.quote_plus(coord_e)
controller.open_new(url)
