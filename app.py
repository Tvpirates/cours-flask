# ========================================
#                 Import
# ========================================
from flask import Flask, render_template
from http import HTTPStatus # Utiliser pour renvoyer des status de page

app = Flask(__name__)

from utils.bundle import assets
# ========================================
#                 Route
# ========================================
@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/hello/<prenom>/<nom>')
def hello(prenom, nom):
    return f"Hello {prenom} {nom} comment vas tu ?", HTTPStatus.CREATED

@app.route('/add/<int:left>/<int:right>')
def addition(left, right):
    return str(5+6), HTTPStatus.CREATED

@app.route('/annee/<int:age>')
def annee(age):
    import datetime  # Import spécifique

    now = datetime.datetime.now()
    return f"Vous êtes né en {now.year - age} et vous avez : {age}"

# 2021 02 03
@app.route('/exercice/cours')
def exerciceCours():
    return render_template('exercice/cours.jinja')


# Affichage quand une erreur 404 est trouvée
@app.errorhandler(404)
def error404(e):
    return render_template('404.jinja')
    # return f"{e}"
