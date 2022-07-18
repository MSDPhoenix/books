from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/authors/')
def authors():
    return render_template('authors.html', authors=Author.get_all())

@app.route('/authors/<int:author_id>/')
def author(author_id):
    data = {
        'author_id':author_id
    }
    author=Author.get_one(data)
    all_books=Book.get_all()
    all_books_ids=[]
    author_favorites_ids=[]
    other_books=[]
    for book in all_books:
        all_books_ids.append(book.id)
    for book in author.favorites:
        author_favorites_ids.append(book.id)
    for book_id in all_books_ids:
        if book_id not in author_favorites_ids:
            other_books.append(Book.get_one({'book_id':book_id}))
    return render_template('author.html',author=author, other_books=other_books)

@app.route('/authors/save/',methods=['POST'])
def author_save():
    data = {
        'name': request.form['name']
        }
    Author.save(data)
    return redirect('/authors/')


@app.route('/authors/add_favorite/<int:author_id>/',methods=['POST'])
def add_favorite_book_to_author(author_id):
    data = {
        'book_id':request.form['book_id'],
        'author_id':author_id
    }
    Author.add_to_favorites(data)
    return redirect('/authors/'+str(author_id))

@app.route('/authors/edit/<int:author_id>/')
def author_edit():
    pass

@app.route('/authors/delete/<int:author_id>/')
def author_delete():
    pass

