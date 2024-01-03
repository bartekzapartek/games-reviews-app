from flask import Flask, Blueprint
from flask import redirect, url_for, render_template

from flask import session

from database.games import get_games_titles

base = Blueprint('base', __name__)

@base.route('/')
def home():
    if 'logged_user' not in session:
        return redirect(url_for('authentication.login'))

    games = get_games_titles()

    return render_template('home.html', games = games)