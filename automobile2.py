#!/usr/bin/python
# -*- coding: utf-8 -*-


def getValue(name):
    total = 0
    for char in name.lower():
        total += ord(char) - 96
    return total

import webbrowser
import urllib
import sys

a = getValue('Porsche')   # goldenes Siegel (Lamborghini oder Porsche)
b = getValue('Opel')      # Rundschild mit Speer (maybe VOLVO?)
c = getValue('Subaru')    # Plejaden
d = getValue('Rover')     # Segelboot (nicht in der EU; westlich der Alpen)
e = getValue('Buick')     # drei Langschilder
f = getValue('Skoda')     # geflügelter Pfeil
g = getValue('Lancia')    # Fahnenmast
h = getValue('Wiesmann')  # Gecko
i = getValue('Maserati')  # Dreizack
j = getValue('Oldsmobile')  # Rakete (Daihatsu?)
k = getValue('Corvette')  # Ziel

# N 46° (B+C-D-1) , (A+C-D+E+F+I+K+4)
# E013° (E-F-G+H+I-J+13) , (A+B+C+D+E+F+G+H+J+34)

# (B+C-D-1)
n1 = b + c - d - 1
#( A+C-D+E+F+I+K+4)
n2 = a + c - d + e + f + i + k + 4
n = 'N 46° ' + str(n1) + '.' + str(n2)

#   (E-F-G+H+I-J+13)
e1 = e - f - g + h + i - j + 13
#   (A+B+C+D+E+F+G+H+J+34)
e2 = a + b + c + d + e + f + g + h + j + 34
e = 'E013° ' + str(e1) + '.' + str(e2)


print n, e
if n1 > 60:
    sys.exit("Latitude is invalid.")
if e1 > 60:
    sys.exit("Longitude is invalid.")

controller = webbrowser.get('safari')
url = 'https://www.google.at/maps/search/'+urllib.quote_plus(n+' ')+urllib.quote_plus(e)
controller.open_new(url)
