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
    
    
#C:\aruna\eclipse\Form_Storage>py.test
#================================================= test session starts =================================================
#platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
#rootdir: C:\aruna\eclipse\Form_Storage
#plugins: flask-0.15.0
#collected 7 items
#
#test_flask_fs.py .......                                                                                         [100%]
# 
#================================================== warnings summary ===================================================
#test_flask_fs.py::test_store
#test_flask_fs.py::test_store_bad
#test_flask_fs.py::test_display
#test_flask_fs.py::test_display_args1
#test_flask_fs.py::test_display_args2
#test_flask_fs.py::test_display_args2_bad
#test_flask_fs.py::test_display_getform
#  c:\users\sachin\appdata\local\programs\python\python37-32\lib\site-packages\flask_sqlalchemy\__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
#    'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '

#-- Docs: https://docs.pytest.org/en/latest/warnings.html
#======================================== 7 passed, 7 warnings in 0.27 seconds =========================================
