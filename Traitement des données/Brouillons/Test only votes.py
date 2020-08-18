import csv
import requests
import config
import smopy

f = open('C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\classement_SSAoG_CSV_V3.csv', 'r')
filename =  csv.reader(f)

Votes = []

for ligne in filename:
    a = ligne[0]
    Votes.append(a)

XP = []
for x in range(len(Votes)):
    e = convertisseur(Votes)
    XP.append(x**2)
    return XP

print(XP)

def convertisseur(converti):
    s = 0
    for i in converti:
        if i < 50:
            s = s+0
        if i >= 50 and i < 100:
            s = s+3
        if i > 100:
            s = s+5
        return s

def liste_XP(Votes):
    XP = []
    for i in range(0,len(g)):
        e = convertisseur(Votes)
        XP.insert(i,x)
        return XP

print(XP)