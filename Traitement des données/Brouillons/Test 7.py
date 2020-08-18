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
print(len(Votes))


def convertisseur(Votes):
    XP = []
    for c in range(len(Votes)):
        convertisseur = lambda c: c==int(3) if c >= 50 and c < 100 else(c==int(5) if c > 100 else c == int(0))
        print(XP)

print(convertisseur(Votes))