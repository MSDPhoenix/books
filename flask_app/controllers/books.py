from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/books/')
def books():
    return render_template('books.html',books=Book.get_all())

@app.route('/books/<int:book_id>/')
def book(book_id):
    this_book=Book.get_one({'book_id':book_id})
    all_authors=Author.get_all()
    favorite_authors_ids=[]
    other_authors=[]
    for author in this_book.favorites:
        favorite_authors_ids.append(author.id)
    for author in all_authors:
        if author.id not in favorite_authors_ids:
            other_authors.append(author)
    return render_template('book.html',book=this_book,other_authors=other_authors)


@app.route('/books/save/',methods=['POST'])
def book_save():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
        }
    Book.save(data)
    return redirect('/books/')

@app.route('/books/add_favorite/<int:book_id>/',methods=['POST'])
def add_favorite_author_to_book(book_id):
    data = {
        'author_id':request.form['author_id'],
        'book_id':book_id
    }
    Book.add_to_favorites(data)
    return redirect('/books/'+str(book_id))

@app.route('/books/update/<int:book_id>/')
def book_update():
    pass

@app.route('/books/edit/<int:book_id>/')
def book_edit():
    pass

@app.route('/books/delete/<int:book_id>/')
def book_delete():
    pass

 