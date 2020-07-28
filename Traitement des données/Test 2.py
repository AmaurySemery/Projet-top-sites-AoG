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
print(tableau0)

#On crée une fonction qui permet d'obtenir les colonnes du tableau CSV

def Colonne_Ligne(tab):
    nb_ligne=len(tab)
    nb_col=len(tab[0])
    tab_lign=[]
    for i in range(nb_col):
        ligne=[]
        for j in range(nb_ligne):
            ligne.append(tab[j][i])
        tab_lign.append(ligne)
    return tab_lign

#On crée une fonction qui va transformer les colonnes du fichier CSV de manière ...
# ... à ce que les valeurs numériques saisies dans le tableur ...
# ...soient des variables de type float dans la liste Python

def Transforme_Ligne(lgn):
    n=len(lgn)   # la taille de la liste est n
    for i in range(1,n):
        # On doit donc remplacer la virgule par un point
        lgn[i]=lgn[i].replace(',','.')
        #Puis on convertit cette chaine de caractère en float
        lgn[i]=float(lgn[i])
    return lgn


#La fonction suivante transforme maintenant toutes les lignes de la variable tableau ...
#....de manière à ce que l'on puisse traiter les données.

def Creation_Tableau(tab):
    m=len(tab)
    for i in range(m):
        tab[i]=Transforme_Ligne(tab[i])
    return tab

#On met les colonnes du tableau CSV dans un tableau
tableau1=Colonne_Ligne(tableau0)
print('on met les colonnes du tableau initiale en ligne\n',tableau1)

#On transforme les valeurs qui sont des string et qui ont des virgules ...
# ...en valeurs numériques avec des points comme séparateur décimal
tableau2=Creation_Tableau(tableau1)

print(tableau2)
