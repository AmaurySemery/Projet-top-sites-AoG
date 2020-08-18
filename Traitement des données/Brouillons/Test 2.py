import csv  #on importe le module csv

#On crée un tableau dans lequel on va mettre les valeurs contenues ...
# ... dans le CSV présenté en colonne
tableau0=[]

with open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV_V2.csv',newline='') as f:    #Ouverture du fichier CSV
    #chargement des lignes du fichier csv
    lire=csv.reader(f,delimiter=';')
    for ligne in lire:              #Pour chaque ligne...
        #print(ligne, end='\n')      #...affichage de la ligne dans la console
        tableau0.append(ligne)        #...on ajoute la ligne dans la liste ...
                                     #...de liste nommée tableau

#On obtient la liste des lignes du tableau


print(tableau0[0])