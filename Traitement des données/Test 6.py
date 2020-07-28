import csv
import requests
import config
import smopy

filename = 'C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\classement_SSAoG_CSV_V2.csv'

def liste_finale(filename):
    XP = []
    f = open('C:\Divers\Python codes\Projet-top-sites-AoG\Dossiers-CSV\classement_SSAoG_CSV_V2.csv', 'r')
    for line in f:
        liste=[]
        Name, Classement, Votes = line.split(',')
        data = {}
        data["Name"]=Name.strip()
        data["Classement"]=Classement.strip()
        data["Votes"]=Votes.strip()
        liste.append(data)
    return liste

print(liste_finale(filename))
