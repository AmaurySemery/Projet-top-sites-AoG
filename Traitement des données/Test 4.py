import csv

def convertisseur('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV_V2.csv'):
#Exemple de chemin :    'C:\\Users\\user\\Desktop\\TIPE\\tableau\\Frequence1_bis.csv'
# /!\ Bien mettre les double slash et les guillemets. /!\
 
 
    #Tableau sera une liste de listes [[t1, acc1], [t2,acc2] ,... , [tn,accn]]
    Tableau = []
    Name = []
    Votes = []
     
    #ouverture et lecture du fichier csv
    f = open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV_V2.csv')
    csv_f = csv.reader(f)
    csv.reader(f, delimiter=';')
     
    # row = ligne ==> ça met le tableur dans le tableau sous forme de liste de listes
    for row in csv_f:
        Tableau.append(row)
    
    f.close
     
    #on récupère les "sous listes" du Tableau
    n = len(Tableau)
    for i in range(n-1):
        Name.append(Tableau[i][0])
        Votes.append(Tableau[i][2])
             
    return (Name, Votes)
