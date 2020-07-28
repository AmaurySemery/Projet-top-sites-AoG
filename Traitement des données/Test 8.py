import csv
import requests
import config
import smopy

f = open('C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\classement_SSAoG_CSV_V2.csv', 'r')
filename =  csv.reader(f)

Name = []
Classement = []
Votes = []
XP = []


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
    g = Votes[:]
    for i in range(0,len(g)):
        e = convertisseur(Votes)
        XP.append(e)
        return XP

for ligne in filename:
    a = ligne[0]
    b = int(ligne[1])
    c = int(ligne[2])
    Name.append(a)
    Classement.append(b)
    Votes.append(c)

XP = liste_XP(Votes)
print(Name)
print(Votes)
print(Classement)
print(XP)
print(len(Votes)) # Compte le nombre d'items de la liste