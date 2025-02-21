from flask import Flask, jsonify, request
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
    return "OK"


@app.route('/user/<username>')
def show_user_profile(username):
    """
    utilisateur par son nom d'utilisateur
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/data')
def data():
    """
    la liste des utilisateurs
    """
    return jsonify(list(users.keys()))


@app.route('/add_user', methods=["POST"])
def add_user():
    """
    Ajouter un nouvel utilisateur via une requête POST
    """
    data = request.get_json() 
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    name = data.get("name")
    age = data.get("age")
    city = data.get("city") 
    if not name or not age or not city:
        return jsonify({"error": "Name, age, and city are required"}), 400
    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
