# Chemin vers le CSV à traiter
myCsvFilePath = "/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade_classement_SSAoG_CSV.csv"
separator = ";"
# Nom de la colonne à supprimer
columnToDeleteName = "NUMVOI"


import csv
import os

myTempOutputFile = myCsvFilePath.replace(".csv", "_tmp.csv")

inFile = open(myCsvFilePath)        
inCSV = csv.reader(inFile, delimiter=separator)
# On commence par rechercher le numero de la colonne à supprimer
firstRow = inCSV.next()
columnIndex = firstRow.index(columnToDeleteName)
inFile.close()

# On va maintenant recopier toutes les lignes du CSV
# dans un nouveau CSV en supprimant la colonne en question
inFile = open(myCsvFilePath)        
inCSV = csv.reader(inFile, delimiter=separator)

outFile = open(myTempOutputFile, 'w+')        
outCSV = csv.writer(outFile, delimiter=separator, quoting=csv.QUOTE_NONNUMERIC)

for row in inCSV:
    # Ici, petite feinte pk Python copie par référence,
    # donc on prend la valeur de la ligne
    # et non la ligne directement
    currentRow = row[:]
    currentRow.pop(columnIndex)
    outCSV.writerow(currentRow)
inFile.close()
outFile.close()

# Là, j'ai créé un csv en plus pour ne pas pêter l'original
# Si, après tes tests, tout fonctionne, tu peux décommenter
# les lignes suivantes :
    
# On supprime le CSV original    
#os.remove(myCsvFilePath)
# On renomme le nouveau CSV avec le nom de l'ancien
#os.rename(myTempOutputFile, myCsvFilePath)

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