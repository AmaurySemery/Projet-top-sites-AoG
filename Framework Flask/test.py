from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
	return "Coucou! <a href='/accueil'> entrez </a>"
	
@app.route('/accueil')
def accueil():
	return "Bienvenue! <a href='/'> retour </a>"
	
@app.route('/pers/<name>')
def pers(name):
	return render_template("page1.html",title="Cool !",username=name)

if __name__ == '__main__':
	app.run()
