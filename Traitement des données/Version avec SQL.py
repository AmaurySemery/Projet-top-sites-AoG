# Placer un except pour faire tourner le programme même si des noms ne correspondent pas à la BDD
# Régler le problème de la ligne qui définit les noms de colonnes. C'est une ligne de commentaire donc elle n'est pas intégrée en l'état dans le programme

## Tu fais la commande "pip install csv" et "pip install pandas" sur le shell pour installer les modules

import csv
import pymysql
import pandas as pd

# Lire le fichier, puis garder les colonnes qui m'intéressent, le nouveau tableau étant envoyé dans un autre fichier


## Ici, tu mets le chemin de ton fichier de base CSV récupéré depuis top-booster (NB : "r" avant le chemin peut ne pas être obligatoire suivant sa structure)
f=pd.read_csv(r"/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV.csv",sep =';',comment='#')
#print(f)

keep_col = ['Pseudo','Total']
#print(keep_col)
new_f = f[keep_col]
#print(new_f)

## Ici, tu mets le chemin de ton deuxième fichier CSV
new_f.to_csv(r"/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade1_classement_SSAoG_CSV.csv", index=False)
#print(keep_col)

# Je récupère le fichier nouvellement créé pour travailler dessus. Je retravaille ensuite le fichier pour supprimer la première ligne, autrement, la chaîne de caractère en première ligne va m'empêcher de faire mes calculs de conversions en int

## Ici, tu mets le chemin de ton deuxième fichier CSV, et pour le lien suivant, celui du troisième fichier

with open(r"/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade1_classement_SSAoG_CSV.csv",'r') as f:
    with open(r"/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade2_classement_SSAoG_CSV.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)

# Je récupère le dernier fichier pour retravailler dessus.
## Ici, tu remets le chemin du troisième fichier CSV qui sera traité pour la suite des opérations

f = open(r'/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade2_classement_SSAoG_CSV.csv', 'r')
filename =  csv.reader(f)

connection = pymysql.connect(host='popschool-willems.fr',
                             user='amaury',
                             password='amaury',
                             db='amaury',
autocommit=True)

cursor = connection.cursor()

## En cas de validation d'un nouveau personnage, l'intégrer ici.
def change(nom):
    request = "SELECT `Police` FROM `Joueurs` WHERE `Nom` LIKE"+ "\"" + nom + "\""
    response = cursor.execute(request)
    if response == True:
        name = cursor.fetchone()
    else:
        name = "Err"
    return str(name[0])

Name = []
Votes = []
XP = []
Final = []

for l in filename:
    a = l[0]
    b = int(l[1])
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