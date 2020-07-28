import csv
import requests
import config
import smopy

f = open('C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\classement_SSAoG_CSV_V2.csv', 'r')
filename =  csv.reader(f)

Name = []
Classement = []
Votes = []

for ligne in filename:
    a = ligne[0]
    b = int(ligne[1])
    c = int(ligne[2])
    Name.append(a)
    Classement.append(b)
    Votes.append(c)

print(Name)
print(Votes)
print(Classement)
print(len(Votes)) # Compte le nombre d'items de la liste

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
    for i in range(len(Votes)):
        d = convertisseur(converti)
        XP.append(d)
        return XP

print(liste_XP(Votes))