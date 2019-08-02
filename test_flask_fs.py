'''
Created on 2 Aug 2019

@author: Aruna
'''

from flask import  url_for
import json


def test_store(client):
    assert client.post(url_for('forms.store'),data=json.dumps(dict(form_field="xyz",value="xyzsda",localisable="Yes"))).status_code == 200
    
def test_store_bad(client):
    assert client.post(url_for('forms.store'),data=json.dumps(dict(value="xyzsda",localisable="Yes"))).status_code == 400
    

def test_display(client):
    assert client.get(url_for('forms.display')).status_code == 200
    
def test_display_args1(client):
    assert client.post(url_for('forms.display'),data=json.dumps(dict(value="xyzsda"))).status_code == 200
    
    
def test_display_args2(client):
    assert client.post(url_for('forms.display'),data=json.dumps(dict(localisable="Yes"))).status_code == 200
    
def test_display_args2_bad(client):
    assert client.post(url_for('forms.display'),data=json.dumps(dict(localisable=1))).status_code == 400
       

def test_display_getform(client):
    assert client.get(url_for('forms.storedid',id=1)).status_code == 200
    

