from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book import Book


@app.route('/books/')
def books():
    return render_template('books.html',books=Book.get_all())

@app.route('/books/<int:book_id>/')
def book(book_id):
    pass


@app.route('/books/save/',methods=['POST'])
def book_save():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
        }
    Book.save(data)
    return redirect('/books/')

@app.route('/books/update/<int:book_id>/')
def book_update():
    pass

@app.route('/books/edit/<int:book_id>/')
def book_edit():
    pass

@app.route('/books/delete/<int:book_id>/')
def book_delete():
    pass

 