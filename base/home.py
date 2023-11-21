from flask import Flask, redirect, url_for
from __main__ import app

@app.route('/')
def home():

    return "Hello world"