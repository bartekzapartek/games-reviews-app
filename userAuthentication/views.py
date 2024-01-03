from flask import render_template
from flask import request, session, redirect, url_for
from flask import Blueprint

from database.authentication import get_user, add_user

from .utils import password_to_hash

authentication = Blueprint('authentication', __name__)

@authentication.route('/login', methods = ['POST', 'GET'])
def login():
    if 'logged_user' in session:
        return redirect(url_for('base.home'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user(username)

        if user is None:
            return redirect(url_for('authentication.login')) 
        
        hash_password = password_to_hash(password)

        if hash_password != user[0][1]:
            return redirect(url_for('authentication.login')) 

        session['logged_user'] = username
        return redirect(url_for('base.home'))


    return render_template('login.html')

@authentication.route('/register', methods = ['POST', 'GET'])
def register():
    if 'logged_user' in session:
        return redirect(url_for('base.home'))

    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = get_user(username, email)

        if user is not None:
            return redirect(url_for('authentication.register'))
        
        hash_password = password_to_hash(password)

        add_user(username, email, hash_password)

        session['logged_user'] = username

        return redirect(url_for('base.home'))
    
    return render_template('register.html')


@authentication.route('/logout', methods = ['POST', 'GET'])
def logout():
    if request.method == "POST":
        session.pop('logged_user', None)
        return redirect(url_for('authentication.login'))

    return render_template('logout.html')

