from flask import Flask, jsonify, request
from database import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    
    # return the data in a dictionnary for the api
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'genre': self.genre}

