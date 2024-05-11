# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    
    if username == 'gayathri' and password == 'ga23':
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)
