import csv
import requests
import config
import smopy

def liste_finale(filename):
    XP = []
    f = open('/home/popschool/Documents/GitHub/Projet-top-sites-AoG/Dossiers-CSV/classement_SSAoG_CSV_V2.csv', 'r')
    for line in f:
        liste=[]
        Name, Classement, Votes = line.split(',')
        data = {}
        data["Name"]=Name.strip()
        data["Classement"]=Classement.string()
        data["Votes"]=Votes.string()
        liste.append(date)
    return liste