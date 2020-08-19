from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
	return "Coucou! <a href='/accueil'> entrez </a>"
	
@app.route('/accueil')
def accueil():
	return "Bienvenue! <a href='/'> retour </a>"
	
@app.route('/pers/<name>/<age>')
def pers(name,age):
	return "hellow " + name + " " + age

if __name__ == '__main__':
	app.run()
