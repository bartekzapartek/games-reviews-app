from flask import render_template, request, session

from __main__ import app


@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        
    return render_template('index.html')
