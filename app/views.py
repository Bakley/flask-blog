"""The main blog file."""
from flask import render_template, flash, url_for, redirect
from app.forms import RegistrationForm, LoginForm
from .import app


@app.route("/")
def home():
    """Root of blog."""
    return render_template('home.html')


@app.route("/about")
def about():
    """About page of blog."""
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for, {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Sign Up', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
