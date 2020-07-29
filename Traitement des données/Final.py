import csv

f = open("yourfile.txt","r")
lines = f.readlines()
f.close()
f = open("yourfile.txt","w")
for line in lines:
  if line!="nickname_to_delete"+"\n":
    f.write(line)
f.close()

f = open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV.csv', 'r')
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
    b = int(l[1])
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