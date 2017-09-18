#!/usr/local/bin/python2
# -*- coding: utf-8 -*-
#
# GC57KJA - Sicherheit und Hilfe
# Status: In Progress...

def getValue(name):
    total = 0
    for char in name.lower():
        if(char != ' '):
            total += ord(char) - 96
    return total

def quersumme(s):
    total = 0
    for z in str(s):
        total += int(z)
    return total

import webbrowser
import urllib
import sys

# 1) Aus wie vielen Sicherheitsbehörden besteht die österreichische Polizei?
#
# die Anzahl = A

a = 4;

# 2) Wann fand die Zusammenlegung statt?
#
# die Quersumme des Datums (TT.MM.JJJJ)  ergibt B

# 1.Juli 2005 => 01.07.2005 => 15
# oder 01.09.2012 => 15

b = 15;

# 3) Wie hieß die Fusion, welche die Zusammenlegung der Wachkörper zusammensetzte? 4 Buchstaben 2 Zahlen
#
# Die Summe ergibt C

# team04 https://de.wikipedia.org/wiki/Zusammenlegung_von_Polizei_und_Gendarmerie
c = getValue('team') + 4;

# 4) Wie heißt die Sondereinsatzeinheit der Wiener Polizei? Abkürzung (4 Buchstaben) umrechnen nach dem Schema A=1, B=2, ..
#
# Die Quersumme der Summe = D

#WEGA
# wegval = getValue('WEGA')
# print('WEGA = ' + str(wegval));
d = quersumme(getValue('WEGA'))

# 5) Wie viele Stützpunkte der Flugpolizei gibt es österreichweit ?
#
# die Anzahl  = E

e = 7

# 6) Wie heißt die kriminalpolizeiliche Datenbank der Polizei? Diese stand auch in der Spitzelaffäre im Mittelpunkt ...  Abkürzung (4 Buchstaben)     Umrechnen nach Schema A=1, B=2,
#
# die Quersumme = F

# EKIS (= Elektronischen Kriminalpolizeilichen Informationssystem)
f = quersumme(getValue('EKIS')) #quersumme???

# 7) Wie viele Mitgliedstaaten hat INTERPOL ? (Stand: Sep. 2013)
#
# die Zahl ergibt  G

g = 190;

# 8) Wie wird der Einsatz einer geschlossenen Einheit der österreichischen Polizei bezeichnet?  Abkürzung (4 Buchstaben) – umrechnen nach Schema A=1, B=2 ..
#
# die Buchstabensumme =  H

h = getValue('GSOD');

# 9) Wo hat der Entschärfungsdienst in Wien seinen Hauptsitz? 2 Worte
#
# Buchstabensumme = I

i = getValue('Rossauerkaserne');

# 10) Wie heißt die Fachzeitschrift des österreichischen Innenministeriums? 2 Worte (Umlaute als AE, OE, UE usw. – umrechnen nach Schema A=1, B=2, ...)
#
# Buchstabensumme = J

# Öffentliche Sicherheit
j = getValue("Oeffentliche Sicherheit")

print "a =", a;
print (b);
print (c);
print (d);
print (e);
print (f);
print (g);
print (h);
print (i);
print (j);


# Die Dose findest du:

#          C x J x A + B x H + I + A = xx.xxx

coord_n1 = c * j * a + b * h + i + a
coord_n1 = coord_n1 / float(1000)

# N 46° xx.xxx
coord_n = 'N 46° ' + str(coord_n1)

#          G x J + ((D + E + F + G) x C ) – 1.145 = yy.yyy

coord_e1 = g * j + ((d + e + f + g) * c) - 1145
coord_e1 = coord_e1 / float(1000)

# E 013° yy.yyy
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
