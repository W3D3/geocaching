#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# GC59Z63


def getValue(name):
    total = 0
    for char in name.lower():
        if(char != ' '):
            total += ord(char) - 96
    return total


def countChars(name):
    total = 0
    for char in name.lower():
        if(char != ' '):
            total += 1
    return total


def quersumme(s):
    total = 0
    for z in str(s):
        total += int(z)
    return total


import webbrowser
import urllib
import sys

# Jynx torquilla
#
# Welches ist die Hauptnahrung des Jynx torquilla? Einzahl – Buchstabensumme = A

a = getValue('Ameise')   # goldenes Siegel (Lamborghini oder Porsche)

# Loxia curvirostra
#
# Die Gelegegröße liegt bei wie vielen Eiern? (selten) die Anzahl = B

b = 5  # Die Gelegegröße liegt bei zwei bis vier Eiern, selten bei fünf Eiern.
#
# Botaurus stellaris
#
# In welchem Roman von Arthur Conan Doyles - Sherlock-Holmes wurde die Botuarus stellaris erwähnt?
# Deutsch = Anzahl der Buchstaben = C

c = countChars('Der Hund von Baskerville')

# Asio otus
#
# Im Winter finden sich gelegentlich Schlafgemeinschaften von Asop otus zusammen, wieviele Exemplare können diese umfassen? Anzahl = D

d = 200  # Im Winter finden sich gelegentlich Schlafgemeinschaften von Waldohreulen zusammen, die bis zu 200 Exemplare umfassen können

# Alcedo atthis
#
# Wann war Alcedo atthis in Österreich „Vogel des Jahres“? Jahreszahl = E

# Der Eisvogel war 1973 und 2009 Vogel des Jahres in Deutschland,[1] 2009 in Österreich, 2005 in Belgien, 2006 Vogel des Jahres in der Schweiz[2] und 2011 in der Slowakei.
e = 2009

# Dendrocopos medius
#
# Die durchschnittliche Größe von den Eiern des Dendrocopos medius? in Millimeter - beide Zahlen multiplizieren ergibt F

f = 23 * 18  # in einer durchschnittlichen Größe von 23 x 18 Millimetern

# Luscinia megarhynchos
#
# Aus welchem Roman von Shakespeare ist unter anderem die bekannte Zeile „Es war die ..... und nicht die Lerche?“  Deutsch – die Quersumme der Summe = G

g = quersumme(getValue('Romeo und Julia'))

# Parus ater
#
# Wann werden die Jungen des Parus ater flügge? max. Tage = H

h = 21  # Die Jungen sind nach 18 bis 21 Tagen flügge.

# Lanius collurio
#
# Wie lange dauert die Großgefiedermauser max.? = I

i = 85  # Die Großgefiedermauser dauert dabei zwischen 80 und 85 Tagen.


# Motacilla flava
#
# Die Körperlänge beträgt bei ausgewachsenen Tieren wieviel max.? = J

j = 16  # Die Körperlänge beträgt bei adulten Tieren 15 bis 16 cm.

# Finde den Cache bei:
#
# N   46° xx.xxx
#
# E 013° yy.yyy
#
#
#
# xx.xxx = F x I + E + B x G – J + 7 + I x B + D - 74
#
coord_n1 = f * i + e + b * g - j + 7 + i * b + d - 74
coord_n1 = coord_n1 / float(1000)

coord_n = 'N 46° ' + str(coord_n1)
#
# yy.yyy = E x C + D x A – (F x B + I x H) – 116 - E + F x 2 - 8
#
#   (E-F-G+H+I-J+13)

coord_e1 = e * c + d * a - (f * b + i * h) - 116 - e + f * 2 - 8
coord_e1 = coord_e1 / float(1000)

coord_e = 'E013° ' + str(coord_e1)


print coord_n, coord_e

if coord_n1 > 60:
    sys.exit("Latitude is invalid.")
if coord_e1 > 60:
    sys.exit("Longitude is invalid.")

controller = webbrowser.get('safari')
url = 'https://www.google.at/maps/search/' + \
    urllib.quote_plus(coord_n + ' ') + urllib.quote_plus(coord_e)
controller.open_new(url)

# FINAL SOLUTION:
# 	N 46°37.811  E 013°47.429
#
#

# Parken kannst du dein Cachemobil bei
# N 46° 37.786
# E 013° 47.490
#
# Viel Spass und happy hunting
#
# kiaw³³
