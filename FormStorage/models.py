'''
Created on 1 Aug 2019

@author: Aruna
'''

from FormStorage import db

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable = False)
    form_fields = db.relationship('Formfield',backref='container',lazy=True)
    
    def __repr__(self):
        return f"{{'id':{self.id}}}"

class Formfield(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    form_field = db.Column(db.String(200), nullable = False)
    value = db.Column(db.String(400), nullable = False)
    localisable = db.Column(db.Boolean, nullable = False)
    form_id = db.Column(db.Integer, db.ForeignKey('form.id'))
    
    