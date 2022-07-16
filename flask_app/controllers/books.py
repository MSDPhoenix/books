from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import book


@app.route('/books')
def books():
    pass

@app.route('/books/<int:book_id>/')
def book(book_id):
    pass


@app.route('/books/save/<int:book_id>/')
def book_save():
    pass

@app.route('/books/update/<int:book_id>/')
def book_update():
    pass

@app.route('/books/edit/<int:book_id>/')
def book_edit():
    pass

@app.route('/books/delete/<int:book_id>/')
def book_delete():
    pass

 