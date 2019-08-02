'''
Created on 1 Aug 2019

@author: Aruna
'''
from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from FormStorage.forms.forms import DataForm, SearchForm
from FormStorage.models import Form, Formfield
from FormStorage import db
from sqlalchemy import desc



forms = Blueprint('forms',__name__)

@forms.route('/',methods=['GET','POST'])
@forms.route('/store',methods=['GET','POST'])
def store():
    content = request.get_json(force=True)
    form_field = None
    value = None
    localisable = None
    for k,v in content.items():
        if k == 'form_field':
            form_field  = v
        elif k == 'value':
            value = v
        elif k == 'localisable':
            if v == 'Yes':
                localisable = True
            elif v == 'No':
                localisable = False
            else:
                abort(400)
            
    if form_field is None or value is None or localisable is None:
        abort(400)
            
    formdata = Form(type='Web')
    db.session.add(formdata)
    db.session.flush()
    getid = formdata.id
    db.session.commit()
    formflddata = Formfield(form_field=form_field, value=value,localisable=localisable, form_id=getid)
    db.session.add(formflddata)
    db.session.commit()
    return "{'id':"+str(getid)+"}"
    #return render_template('store.html',title = 'Store', form=form)

@forms.route('/storedid/<id>',methods=['GET'])
def storedid(id):
    data = Formfield.query.filter_by(form_id=id).first_or_404()
    return render_template('storedid.html',title = 'ID of stored form', id=id,data=data)
     

@forms.route('/retrieve',methods=['GET','POST'])
def retrieve():
    form = SearchForm()
    if form.validate_on_submit():
        value = form.value.data
        localisable=form.localisable.data
        if value == '':
            value = 'value'
        if localisable == '':
            localisable = 'localisable'
        return redirect(url_for('forms.display'))
    return render_template('retrieve.html',title = 'retrieve', form=form)

@forms.route('/display',methods=['GET','POST'])
def display():
    if request.method == 'GET':
        formdata = Formfield.query.order_by(Formfield.id)
        return render_template('display.html',title = 'display', formdata=formdata)
        
    content = request.get_json(force=True)
    localisable = None
    value = None
    for k,v in content.items():
        if k == 'localisable':
            localisable  = v
        elif k == 'value':
            value = v
        else:
            abort(400)
    if localisable is not None:
        if localisable == 'Yes':
            localisable = True
        elif localisable == 'No':
            localisable = False
        else:
            abort(400)
    if value is not None and localisable is not None:
        formdata = Formfield.query.filter_by(value = value, localisable = localisable)
    elif value is not None:
        formdata = Formfield.query.filter_by(value = value)
    elif localisable is not None:
        formdata = Formfield.query.filter_by(localisable = localisable)
    else:
        formdata = Formfield.query.order_by(Formfield.id)
    return render_template('display.html',title = 'display', formdata=formdata)
        
        
    
    