from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/user/<username')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/data')
def data():
    if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
            return jsonify()
    
@app.route('/add_user')
def user():
    pass

if __name__ == "__main__":
    app.run()
