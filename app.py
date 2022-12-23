from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

responses = []

