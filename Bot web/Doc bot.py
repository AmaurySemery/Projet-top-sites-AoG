# Urllib et Urllib2 : permettent de gérer des requêtes web simples
# Cookielib : permet de gérer les cookies

import urllib2

url = 'http://www.google.fr'
req = urllib2.Request(url)
reponse = urllib2.urlopen(req)
html = reponse.read()

# Nous voulons voir la page http://www.google.fr, on utilise urllib2.request pour préparer la requête que l'on va stocker dans req, ensuite on exécute cette dernière via urlib2.urlopen.
# Cette fonction nous renvoie la réponse du serveur web mais ici nous voulons récupérer le html de la page, on utilise reponse.read pour cela.

import urllib
import urllib2

url = 'http://server.com/post_data.php'
values = {'name':'Pasterp',
'pass':'kangourou',
'message':'Python !'} #Valeurs d'un formulaire web

data = urllib.urlencode(values)
req = urllib2.Request(the_url, data)
handle = urllib2.urlopen(req)

