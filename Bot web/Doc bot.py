# Urllib et Urllib2 : permettent de gérer des requêtes web simples
# Cookielib : permet de gérer les cookies

import urllib2

url = 'http://www.google.fr'
req = urllib2.Request(url)
reponse = urllib2.urlopen(req)
html = reponse.read()

# Via la page http://www.google.fr, on utilise urllib2.request pour préparer la requête que l'on va stocker dans req, ensuite on exécute cette dernière via urlib2.urlopen.
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

# Nous allons ici simuler l'envoie du resultat d'un formulaire HTML. values contient les différents champs du formulaire et leur valeurs (ici : name, pass et message).
# On utilise urlib.urlencode pour encoder ces valeurs avant de les passer à la fonction urllib2.Request et ensuite on agit de même que dans la première partie.

import urllib
import urllib2

url = 'http://server.com/post_data.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name':'Pasterp',
'pass':'kangourou',
'message':'Python !'} #Valeurs d'un formulaire web
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(the_url, data, headers)
handle = urllib2.urlopen(req)

# Les sites web peuvent vous identifier grâce aux headers de vos requêtes web tel que user-gent qui identifie votre navigateur, referer qui permet au site de savoir d'ou vous venez...
# Nous allons pour indiquer au site ces infos reprendre l'exemple précédant.
# Bien sur il suffit de faire de même avec les autres paramètres du headers.

import urllib
import urllib2
import cookielib

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urlOpener.addheaders = [{'User-agent', user_agent}]

url = 'http://www.google.fr'
req = urllib2.Request(url)
reponse = urlOpener(req)
html = reponse.read()

# Les sites web utilisent les cookies pour vous reconnaitre de manière plus sécurisée, par exemple lors de la connexion sur un site un cookies se crée pour que le site sache que vous êtes connecté tandis que vous changer de pages.
# Pour pouvoir utiliser les cookies et être identifié par le site, nous allons utiliser un cookiejar (en français un pot de cookies ça donne très faim). Ce dernier va stocker les cookies qu'il recevra. Pour l'intégrer dans nos requêtes, on doit créer un Url_opener, qui est la fonction envoyant la requête au serveur (comme la fonction openurl que nous avons vu. Cet url_opener va gerer de manière interne les headers (dont les cookies font parties), dont on a la possibilité d'en ajouter (comme ci dessus pour le user-agent).