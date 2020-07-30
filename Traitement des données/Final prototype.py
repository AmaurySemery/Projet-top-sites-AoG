import csv

# Lire le fichier, puis garder les colonnes qui m'intéressent, le nouveau tableau étant envoyé dans un autre fichier

import pandas as pd
f=pd.read_csv(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade_classement_SSAoG_CSV.csv",sep =';')
#print(f)
keep_col = ['Pseudo','Total']
#print(keep_col)
new_f = f[keep_col]
#print(new_f)
new_f.to_csv(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade1_classement_SSAoG_CSV.csv", index=False)
#print(keep_col)

# Je récupère le fichier nouvellement créé pour travailler dessus. Je retravaille ensuite le fichier pour supprimer la première ligne, autrement, la chaîne de caractère en première ligne va m'empêcher de faire mes calculs de conversions en int

with open(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade1_classement_SSAoG_CSV.csv",'r') as f:
    with open(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade2_classement_SSAoG_CSV.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)

# Je récupère le dernier fichier pour retravailler dessus.

f = open(r'C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade2_classement_SSAoG_CSV.csv', 'r')
filename =  csv.reader(f)



def conversion(number):
    if number < 50:
        result = 0
    if number >= 50 and number < 100:
        result = 3
    if number > 100:
        result = 5
    return result
    #print(+ int(result))

Name = []
Votes = []
XP = []
Final = []

for l in filename:
    a = l[0]
    b = int(l[1])
    Name.append(a)
    Votes.append(b)
    XP.append(conversion(b))

# print(Name,Votes,XP)

datedebut = input("Date début de requête (ex: 22/06): ")
datefin = input("Date fin de requête (ex: 28/06): ")

print("<blockquote>[center][b]Récompenses du "+datedebut+" au "+datefin+"[/b][/center]")
print("Pour rappel, vous gagnez 3 XP par semaine si vous effectuez au moins <b>50</b> votes sur celle-ci.")
print("Vous gagnez 5 XP au total si vous êtes parmi les 5 meilleurs votants ou que vous avez réalisé plus de 100 votes.")
print("Les récompensés sont donc les suivants :[list=1]")

for x,y in zip(Name,XP):
    a = x
    b = y
    Final.append(a)
    Final.append(b)
    #print([x,y])
    print("[*][b]"+ x+ "[/b]",":", y,"XP")

print("[/list]")

print("AoG compte", len(Votes),"votants pour cette session.")