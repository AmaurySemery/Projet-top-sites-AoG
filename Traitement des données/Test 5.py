import csv

    #Tableau sera une liste de listes [[t1, acc1], [t2,acc2] ,... , [tn,accn]]
Tableau = []
Name = []
Classement = []
Votes = []
     
    #ouverture et lecture du fichier csv
f = open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV_V2.csv')
csv_f = csv.reader(f)
     
    # row = ligne ==> ça met le tableur dans le tableau sous forme de liste de listes
for row in csv_f:
    Tableau.append(row)
    
f.close
     
    #on récupère les "sous listes" du Tableau
n = len(Tableau)
for i in range(n-1):
    Name.append(Tableau[i][0])
    Classement.append(int(Tableau[i][1]))
    Votes.append(int(Tableau[i][2]))

print(Name, Classement, Votes)

NameV2 = Name[0:30]
ClassementV2 = Classement[0:30]
VotesV2 = Votes[0:30]

print(NameV2[0],ClassementV2[0],VotesV2[0])

def liste_finale():
    XP = []
    for line in f:
        