# Chemin vers le CSV à traiter
myCsvFilePath = '/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade_classement_SSAoG_CSV.csv'
separator = ';'
# Nom de la colonne à supprimer
columnToDeleteName = "NUMVOI"

import csv
import os

myTempOutputFile = myCsvFilePath.replace(".csv", "_tmp.csv")

inFile = open(myCsvFilePath)
inCSV = csv.reader(inFile, delimeter=separator)

# On commence par rechercher le numéro de la colonne à supprimer

firstRow = inCSV.next()
columnIndex = firstRow.index(columnToDeleteName)
inFile.close()

f = open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade_classement_SSAoG_CSV.csv', 'r')
filename =  csv.reader(f)


def conversion(number):
    if number < 50:
        result = 0
    if number >= 50 and number < 100:
        result = 3
    if number > 100:
        result = 5
    return result
    #    print(+ int(result))

Name = []
Votes = []
XP = []
Final = []

for l in filename:
    a = l[0]
    b = l[1]
    Name.append(a)
    Votes.append(b)
    XP.append(conversion(b))
    

# print(Name,Votes,XP)

for x,y in zip(Name,XP):
    a = x
    b = y
    Final.append(a)
    Final.append(b)
    print([x,y])

print("AoG compte", len(Votes),"votants pour cette session.")