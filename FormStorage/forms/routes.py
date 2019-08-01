'''
Created on 1 Aug 2019

@author: Aruna
'''
from flask import render_template, url_for, flash, redirect,  Blueprint
from FormStorage.forms.forms import DataForm, SearchForm
from FormStorage.models import Form, Formfield
from FormStorage import db
from sqlalchemy import desc


forms = Blueprint('forms',__name__)

@forms.route('/',methods=['GET','POST'])
@forms.route('/store',methods=['GET','POST'])
def store():
    form = DataForm()
    if form.validate_on_submit():
        formdata = Form(type='Web')
        db.session.add(formdata)
        db.session.flush()
        getid = formdata.id
        db.session.commit()
        formflddata = Formfield(form_field=form.form_field.data, value=form.value.data,localisable=form.localisable.data, form_id=getid)
        db.session.add(formflddata)
        db.session.commit()
        flash(f'Data has been stored!', 'success')
        return redirect(url_for('forms.storedid',id=getid))
    return render_template('store.html',title = 'Store', form=form)

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
        return redirect(url_for('forms.display',value=value,localisable=localisable))
    return render_template('retrieve.html',title = 'retrieve', form=form)

@forms.route('/display/<string:value>/<string:localisable>',methods=['GET'])
def display(value,localisable):
    if localisable != 'localisable':
        if localisable == 'Yes':
            localisable = True
        elif localisable == 'No':
            localisable = False
    if value != 'value' and localisable != 'localisable':
        formdata = Formfield.query.filter_by(value = value, localisable = localisable)
    elif value != 'value':
        formdata = Formfield.query.filter_by(value = value)
    elif localisable != 'localisable':
        formdata = Formfield.query.filter_by(localisable = localisable)
    else:
        formdata = Formfield.query.order_by(Formfield.id)
    return render_template('display.html',title = 'display', formdata=formdata)
        
        
    
    