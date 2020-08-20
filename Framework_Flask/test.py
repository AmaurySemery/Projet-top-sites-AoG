from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
	return "Coucou! <a href='/accueil'> Accès à l'accueil </a>" + " " + "Hellow <a href='/pers/<name>'> Onglet pers </a>"
	
@app.route('/accueil')
def accueil():
	return "Bienvenue! <a href='/'> retour </a>" + " " + "Hellow <a href='/pers/<name>'> Onglet pers </a>"
	
@app.route('/pers/<name>')
def pers(name):
	return render_template("page1.html",title="Cool !",username=name) + "Hellow <a href='/accueil'> retour </a>"

if __name__ == '__main__':
	app.run()
