#ouverture d'un fichier CSV...
#... création de la liste des lignes nommée tableau...
#... et affichage des lignes.
import csv
with open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV_V2.csv',newline='') as f:
    tableau=[]
    lire= csv.reader(f)
    for row in reader:
        print(row)