from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def load_dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    data = { 'name' : request.form['new_dojo'] }
    Dojo.create(data)
    return redirect('/dojos')

@app.route('/ninja_list/<dojo_id>')
def ninja_list(dojo_id):
    data = { 'dojo_id' : dojo_id }
    dojo = Dojo.get_one(data)[0]
    ninjas = Ninja.get_dojo_roster(data)
    return render_template('ninja_list.html', dojo=dojo, ninjas=ninjas)

@app.route('/new_ninja')
def new_ninja_form():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        'dojo_id' : request.form['dojo'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    Ninja.create(data)
    return redirect('/ninja_list/' + data['dojo_id'])