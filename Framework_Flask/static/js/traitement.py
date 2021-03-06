# -*- coding: utf-8 -*-
# Placer un except pour faire tourner le programme même si des noms ne correspondent pas à la BDD
# Régler le problème de la ligne qui définit les noms de colonnes. C'est une ligne de commentaire donc elle n'est pas intégrée en l'état dans le programme

## Tu fais la commande "pip install csv" et "pip install pandas" sur le shell pour installer les modules

import csv
import pymysql
import pandas as pd
import os, glob


## En cas de validation d'un nouveau personnage, l'intégrer ici.
def change(nom):
    request = "SELECT `Police` FROM `Joueurs` WHERE `Nom` LIKE"+ "\"" + nom + "\""
    response = cursor.execute(request)
    if response == True:
        name = cursor.fetchone()
    else:
        name = "Err"
    return str(name[0])

# Lire le fichier, puis garder les colonnes qui m'intéressent, le nouveau tableau étant envoyé dans un autre fichier


## Ici, tu mets le chemin de ton fichier de base CSV récupéré depuis top-booster (NB : "r" avant le chemin peut ne pas être obligatoire suivant sa structure)

f=open(r"/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV.csv")

r = csv.DictReader(filter(lambda row: row[0]!='#',f), fieldnames = ["Pseudo", "Classement", "IDmark", "IDmark2", "Total"], delimiter = ";")
# Je récupère le dernier fichier pour retravailler dessus.
## Ici, tu remets le chemin du troisième fichier CSV qui sera traité pour la suite des opérations

connection = pymysql.connect(host='popschool-willems.fr',
                             user='amaury',
                             password='amaury',
                             db='amaury',
autocommit=True)

cursor = connection.cursor()

Name = []
Votes = []
XP = []
Final = []
for row in r:
    a = row['Pseudo']
    b = int(row['Total'])
    Name.append(a)
    Votes.append(b)
    if b < 50:
        result = 0
    if b >= 50 and b < 100:
        result = 3
    if b > 100:
        result = 5
    XP.append(result)

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
    print("[*][b]"+change(x)+"[/color][/b]",":", y,"XP")

print("[/list]")

print("AoG compte", len(Votes),"votants pour cette session.")
print("Merci à vous et bon jeu sur AoG !")
print("--------")
print("Légende :")
print("Saint : [color=#4A6A87]")
print("Berserker : [color=#A21713]")
print("Marina : [color=#228A94]")
print("Oracle : [color=#B47C1C]")