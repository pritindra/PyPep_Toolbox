from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Defining Models for user
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    def hash_password(self,password):
        self.password_hash = generate_password_hash(password)
    
if os.path.exists("user.db"):
    os.remove("slam.db")

db.create_all()

# LOGIN SYSTEM
@app.route('/login', methods = ['GET'])
@auth.verify_password
def verify_password(username,password):
    if username in user and check_password_hash(user.get(username),password):
        return username

# ROOT 
@app.rouete('/home')
def index():
    return {'message': "Hello world"}

if __name__ == '__main__':
    app.run(debug = True)