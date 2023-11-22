from flask import render_template
from flask import request, session, redirect, url_for
from flask import Blueprint

from database.authentication import get_user, add_user

authentication = Blueprint('authentication', __name__)

@authentication.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user(username)

        if user is None:
            return redirect(url_for('authentication.login')) 
        
        session['user'] = username

    return render_template('login.html')

@authentication.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = get_user(username)

        if user is not None:
            return redirect(url_for('authentication.register'))
        
        add_user(username, email, password)

        return redirect(url_for('base.home'))
    
    return render_template('register.html')

@authentication.route('/logout', methods = ['POST', 'GET'])
def logout():
    if request.method == "POST":
        pass

