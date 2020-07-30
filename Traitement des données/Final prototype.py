import csv

with open("/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade_classement_SSAoG_CSV.csv","rb") as source:
    rdr= csv.reader( source )
with open("/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade1_classement_SSAoG_CSV.csv","wb") as result:
    wtr = csv.writer( result )
    for r in rdr:
        wtr.writerow((r[0], r[1]))

in_iter= ( (r[0], r[1], r[3], r[4]) for r in rdr )
wtr.writerows( in_iter )

del r[1], r[3], r[4]
wtr.writerow( r )

f = open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/upgrade_classement_SSAoG_CSV.csv', 'r')
filename =  csv.reader(f)


def conversion(number):
    if number < 50:
        result = 0
    if number >= 50 and number < 100:
        result = 3
    if number > 100:
        result = 5
    return result
    #    print(+ int(result))

Name = []
Votes = []
XP = []
Final = []

for l in filename:
    a = l[0]
    b = l[1]
    Name.append(a)
    Votes.append(b)
    XP.append(conversion(b))
    

# print(Name,Votes,XP)

for x,y in zip(Name,XP):
    a = x
    b = y
    Final.append(a)
    Final.append(b)
    print([x,y])

print("AoG compte", len(Votes),"votants pour cette session.")