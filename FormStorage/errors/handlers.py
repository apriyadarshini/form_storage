'''
Created on 1 Aug 2019

@author: Aruna
'''

from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404