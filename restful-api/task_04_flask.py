from flask import Flask, jsonify, request
"""
Initialisation de l'application Flask
"""
app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    Page d'accueil de l'API
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    Vérifie l'état du serveur
    """
    return "OK"


@app.route('/users/<username>')
def show_user_profile(username):
    """
    Récupère le profil d'un utilisateur par son nom d'utilisateur
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/data')
def data():
    """
    Retourne la liste des utilisateurs
    """
    return jsonify(list(users.keys()))


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Retourne un dico
    """
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
