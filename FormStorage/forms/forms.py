'''
Created on 1 Aug 2019

@author: Aruna
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    form_field = StringField('Form Field',validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    
    localisable = BooleanField('localisable')
    submit = SubmitField('Submit')
    
class SearchForm(FlaskForm):
    value = StringField('Value')
    localisable = StringField('localisable')
    submit = SubmitField('Submit')
    
    
    
