from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import book

@app.route('/authors/')
def authors():
    return render_template('authors.html')

@app.route('/authors/<int:author_id>/')
def author(author_id):
    pass


@app.route('/authors/save/',methods=['POST'])
def author_save():
    pass


@app.route('/authors/update/<int:author_id>/')
def author_update():
    pass

@app.route('/authors/edit/<int:author_id>/')
def author_edit():
    pass

@app.route('/authors/delete/<int:author_id>/')
def author_delete():
    pass

