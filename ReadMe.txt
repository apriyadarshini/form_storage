How to run Form Data Storage locally:

1) Install the packages present in requirements.txt
2) import create_app from FormStorage
3) Initialize the app variable to create_app()
4) create all tables within this app context by importing all the tables present in FormStorage.models
5) export FLASK_APP=run.py
6) flask run --host=0.0.0.0
7) Open http://localhost:5000/ in a web browser

Solution is scalable as each feature is a separate Blueprint. 
If a new feature needs to be added we can create a new package and create a Blueprint of it and register it with the app.

Currently front end has been provided for the app to store and retrieve data

We can also easily modify it (in FormStorage.forms.routes module) to use json input if front end is not required.

To store bulk data we can have the bulk input in a json file and load from the file using json package into a dictionary and loop over it to create instances of classes present in FormStorage.models reflecting the tables and store them in the tables 

Complete detail about the classes and modules is present in FormStorage.docx
 
********************************************************
Testing:
********************************************************

pytest:
  
  pip install pytest-flask
  py.test

Tests are present in test_flask_fs.py

curl commands to:

store data: 
curl --request POST --data '{"form_field":"xyz","value":"xyzsda","localisable":"Yes"}' http://localhost:5000

get the data for a given id: 
curl  http://localhost:5000/storedid/<id>

query based on value and/or localisable fields:
 curl --request POST --data '{"value":"xyzsda","localisable":"Yes"}' http://localhost:5000/display
 curl --request POST --data '{"value":"xyzsda"}' http://localhost:5000/display
 curl http://localhost:5000/display
  
  
