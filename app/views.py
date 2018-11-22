"""The main blog file."""
from flask import render_template
from .import app


@app.route("/")
def home():
    """Root of blog."""
    return render_template('home.html')


@app.route("/about")
def about():
    """About page of blog."""
    return render_template('about.html')
