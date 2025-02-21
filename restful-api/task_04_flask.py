from flask import Flask
from flask import jsonify
from flask import request
"""
Initialisation de l'application Flask
"""
app = Flask(__name__)

users = {
            "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
            "john": {"username": "john", "name": "John", "age": 30,
                     "city": "New York"}}


@app.route('/')
def home():
    """
    page d'accueil
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    l'état du serveur
    """
    return ("OK")


@app.route('/user/<username>')
def show_user_profile(username):
    """
    utilisateur par son nom d'utilisateur
    """
    user = users.get(username)
    if user:
        return jsonify(user)


@app.route('/data')
def data():
    """
    la liste des utilisateurs
    """
    return jsonify(list(users.keys()))


@app.route('/add_user')
def user():
    """
    ajouter un nouvel utilisateur
    """
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400


if __name__ == "__main__":
    app.run()
