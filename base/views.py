from flask import Flask, Blueprint, redirect, url_for, render_template

base = Blueprint('base', __name__)

@base.route('/')
def home():

    return render_template('login.html')