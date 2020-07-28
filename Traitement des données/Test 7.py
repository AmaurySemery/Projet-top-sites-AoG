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
    b = ligne[1]
    c = int(ligne[2])
    Name.append(a)
    Classement.append(b)
    Votes.append(c)

print(Name)
print(Classement)
print(Votes)


def convertisseur(Votes):
    XP = []
    for c in range(c+1):
        convertisseur = lambda c: c==int(3) if c >= 50 and c < 100 else(c==int(5) if c > 100 else c == int(0))
        print(XP)

print(convertisseur(Votes))


def conversion(c):
    if c < 50:
        return 0
    elif c >= 50 and c < 100:
        return 3
    else:
        return 5

print(map(conversion, Votes))

def liste_finale(filename):
    XP = []
    f = open('C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\classement_SSAoG_CSV_V2.csv', 'r')
    for line in f:
        liste=[]
        Name, Classement, Votes = line.split(',')
        data = {}
        data["Name"]=Name.strip()
        data["Classement"]=Classement.strip()
        data["Votes"]=Votes.strip()
        liste.append(data)
    return liste

# print(liste_finale(filename))
