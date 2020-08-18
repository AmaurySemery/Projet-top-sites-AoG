import csv
 
with open("/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/table01.csv", "r") as fsrce:
    with open("table02.csv", "w", newline='') as fdest:
        my_reader = csv.reader(fsrce, delimiter = ';')
        my_writer = csv.writer(fdest, delimiter = ';')
        for ligne in my_reader: # ligne est une liste de valeurs de colonnes
            print(my_writer.writerow(ligne[0]))
# ligne[0] est la valeur de la 1ère colonne de la ligne considéré

import csv
 
with open("/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/table01.csv", "r") as fsrce:
    with open("table02.csv", "w") as fdest:
        my_reader = csv.reader(fsrce, delimiter = ';')
        for ligne in my_reader:
            fdest.write(ligne[0] + '\n')
            print(fdest.write(ligne[0] + '\n'))