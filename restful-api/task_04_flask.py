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


@app.route('/add_user', methods=["POST"])
def add_user():
    """
    un nouvel utilisateur via une requête POST
    """
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400
    if not name or not age or not city:
        return jsonify({"error": "Name, age, and city are required"}), 400
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
