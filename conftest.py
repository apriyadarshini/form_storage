'''
Created on 2 Aug 2019

@author: Aruna
'''

from FormStorage import create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app


