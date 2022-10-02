import os
from flask import Flask, jsonify, request 
from flask_httpauth import HTTPDigestAuth
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Senam'
auth = HTTPDigestAuth()

users = {
    'vcu': 'rams'
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/pong', methods=['GET'])
@auth.login_required
def pongService():
    pong =random.randint(1, 999999)
    
    return jsonify(str(pong))




if __name__ == '__main__':
    app.run()