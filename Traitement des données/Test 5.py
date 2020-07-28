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

import pandas as pd

# the file names
f1 = Name
f2 = Classement
f3 = Votes
out_f = "/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/tableau_test.csv"

# read the files
df1 = pd.read_csv(f1)
df2 = pd.read_csv(f2)
df3 = pd.read_csv(f3)

# get the keys
keys1 = list(df1)
keys2 = list(df2)
keys3 = list(df3)

# merge both files
for idx, row in df2.iterrows():
    data = df1[df1['id'] == row['id']]

    # if row with such id does not exist, add the whole row
    if data.empty:
        next_idx = len(df1)
        for key in keys2:
            df1.at[next_idx, key] = df2.at[idx, key]

    # if row with such id exists, add only the missing keys with their values
    else:
        i = int(data.index[0])
        for key in keys2:
            if key not in keys1:
                df1.at[i, key] = df2.at[idx, key]

# save the merged files
df1.to_csv(out_f, index=False, encoding='utf-8', quotechar="", quoting=csv.QUOTE_NONE)