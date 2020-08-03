## Tu fais la commande "pip install csv" et "pip install pandas" sur le shell pour installer les modules

import csv

# Lire le fichier, puis garder les colonnes qui m'intéressent, le nouveau tableau étant envoyé dans un autre fichier

import pandas as pd
## Ici, tu mets le chemin de ton fichier de base CSV récupéré depuis top-booster (NB : "r" avant le chemin peut ne pas être obligatoire suivant sa structure)
f=pd.read_csv(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade_classement_SSAoG_CSV.csv",sep =';')
#print(f)
keep_col = ['Pseudo','Total']
#print(keep_col)
new_f = f[keep_col]
#print(new_f)

## Ici, tu mets le chemin de ton deuxième fichier CSV
new_f.to_csv(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade1_classement_SSAoG_CSV.csv", index=False)
#print(keep_col)

# Je récupère le fichier nouvellement créé pour travailler dessus. Je retravaille ensuite le fichier pour supprimer la première ligne, autrement, la chaîne de caractère en première ligne va m'empêcher de faire mes calculs de conversions en int

## Ici, tu mets le chemin de ton deuxième fichier CSV, et pour le lien suivant, celui du troisième fichier

with open(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade1_classement_SSAoG_CSV.csv",'r') as f:
    with open(r"C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\upgrade2_classement_SSAoG_CSV.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)

# Je récupère le dernier fichier pour retravailler dessus.
## Ici, tu remets le chemin du troisième fichier CSV qui sera traité pour la suite des opérations

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

## En cas de validation d'un nouveau personnage, l'intégrer ici.
def change(nom):
    #Berserkers
    if nom == 'Alastair':
        nom = '[color=#A21713]Alastair'
    if nom == 'Aelinor':
        nom = '[color=#A21713]Aelinor'
    if nom == 'Akir':
        nom = '[color=#A21713]Akir'
    if nom == 'Bran Ruz':
        nom = '[color=#A21713]Bran Ruz'
    if nom == 'Brohos':
        nom = '[color=#A21713]Brohos'
    if nom == 'César':
        nom = '[color=#A21713]César'
    if nom == 'Chris':
        nom = '[color=#A21713]Chris'
    if nom == 'Elyra':
        nom = '[color=#A21713]Elyra'
    if nom == 'Esther':
        nom = '[color=#A21713]Esther'
    if nom == 'Haldor':
        nom = '[color=#A21713]Haldor'
    if nom == 'Jehane':
        nom = '[color=#A21713]Jehane'
    if nom == 'Liv':
        nom = '[color=#A21713]Liv'
    if nom == 'Lymsleia':
        nom = '[color=#A21713]Lymsleia'
    if nom == 'Merion':
        nom = '[color=#A21713]Mérion'
    if nom == 'Satine':
        nom = '[color=#A21713]Satine'
    if nom == 'Velizara':
        nom = '[color=#A21713]Velizara'
    if nom == 'Zvezdan':
        nom = '[color=#A21713]Zvezdan'
    #Saints
    if nom == 'Aegis':
        nom = '[color=#4A6A87]Aegis'
    if nom == 'Airoth':
        nom = '[color=#4A6A87]Airoth'
    if nom == 'Algebar':
        nom = '[color=#4A6A87]Algebar'
    if nom == 'Argus':
        nom = '[color=#4A6A87]Argus'
    if nom == 'Childeric':
        nom = '[color=#4A6A87]Childéric'
    if nom == 'Diane':
        nom = '[color=#4A6A87]Diane'
    if nom == 'Elias':
        nom = '[color=#4A6A87]Elias'
    if nom == 'Eudoxia':
        nom = '[color=#4A6A87]Eudoxia'
    if nom == 'Khoren':
        nom = '[color=#4A6A87]Khoren'
    if nom == 'Kilian':
        nom = '[color=#4A6A87]Kilian'
    if nom == 'Lesath':
        nom = '[color=#4A6A87]Lesath'
    if nom == 'Mehry':
        nom = '[color=#4A6A87]Mehry'
    if nom == 'Morwenna':
        nom = '[color=#4A6A87]Morwenna'
    if nom == 'Nebu':
        nom = '[color=#4A6A87]Nebu'
    if nom == 'Odoroi':
        nom = '[color=#4A6A87]Odoroï'
    if nom == 'Paros':
        nom = '[color=#4A6A87]Paros'
    if nom == 'Ryme':
        nom = '[color=#4A6A87]Ryme'
    if nom == 'Sighild':
        nom = '[color=#4A6A87]Sighild'
    if nom == 'Silas':
        nom = '[color=#4A6A87]Silas'
    if nom == 'Tharros':
        nom = '[color=#4A6A87]Tharros'
    if nom == 'Theolus':
        nom = '[color=#4A6A87]Theolus'
    if nom == 'Xanathos':
        nom = '[color=#4A6A87]Xanathos'
    #Marinas
    if nom == 'Aimana':
        nom = '[color=#228A94]Aimana'
    if nom == 'Asteria':
        nom = '[color=#228A94]Asteria'
    if nom == 'Calypso':
        nom = '[color=#228A94]Calypso'
    if nom == 'Dardanos':
        nom = '[color=#228A94]Dardanos'
    if nom == 'Deukalyion':
        nom = '[color=#228A94]Deukalyion'
    if nom == 'Drystan':
        nom = '[color=#228A94]Drystan'
    if nom == 'Emrys':
        nom = '[color=#228A94]Emrys'
    if nom == 'Endymion':
        nom = '[color=#228A94]Endymion'
    if nom == 'Lazare':
        nom = '[color=#228A94]Lazare'
    if nom == 'Orpheus':
        nom = '[color=#228A94]Orpheus'
    if nom == 'Selena':
        nom = '[color=#228A94]Selena'
    #Oracles
    if nom == 'Adonis':
        nom = '[color=#B47C1C]Adonis'
    if nom == 'Celestia':
        nom = '[color=#B47C1C]Celestia'
    if nom == 'Cuchulainn':
        nom = '[color=#B47C1C]Cuchulainn'
    if nom == 'Diogene':
        nom = '[color=#B47C1C]Diogène'
    if nom == 'Esmelia':
        nom = '[color=#B47C1C]Esmelia'
    if nom == 'Kyrios':
        nom = '[color=#B47C1C]Kyrios'
    if nom == 'Lykeios':
        nom = '[color=#B47C1C]Lykeios'
    if nom == 'Rowena':
        nom = '[color=#B47C1C]Rowena'
    if nom == 'Rudjek':
        nom = '[color=#B47C1C]Rudjek'
    if nom == 'Sunilda':
        nom = '[color=#B47C1C]Sunilda'
    if nom == 'Yelo':
        nom = '[color=#B47C1C]Yelo'
    else:
        nom = nom
    return nom

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
    print("[*][b]"+change(x)+"[/color][/b]",":", y,"XP")

print("[/list]")

print("AoG compte", len(Votes),"votants pour cette session.")
print("--------")
print("Légende :")
print("Saint : [color=#4A6A87]")
print("Berserker : [color=#A21713]")
print("Marina : [color=#228A94]")
print("Oracle : [color=#B47C1C]")