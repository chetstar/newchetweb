from app import app
from flask import Flask, render_template, send_from_directory, request, flash
from forms import ContactForm

app.secret_key = 'development key'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    form = ContactForm()
    return render_template('index.html', form=form)