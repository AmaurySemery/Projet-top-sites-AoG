import csv
with open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers CSV/classement_SSAoG_CSV.csv', newline'') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
