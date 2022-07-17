from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author():
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors;'
        results = connectToMySQL('books').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM authors WHERE id=%(author_id)s;'
        result = connectToMySQL('books').query_db(query,data)
        # print("result[0] = ",result[0])
        author = cls(result[0])
        author.favorites=book.Book.get_favorites(data)
        return author

    @classmethod
    def get_favorites(cls,data):
        query = '''
                SELECT * FROM authors
                LEFT JOIN favorites ON authors.id = favorites.author_id
                WHERE favorites.book_id = %(book_id)s;
                '''
        results = connectToMySQL('books').query_db(query,data)
        favorites = []
        for author in results:
            favorites.append(cls(author))
        return favorites

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO authors (name)
                VALUES (%(name)s)
                """
        return connectToMySQL('books').query_db(query,data)

    def add_to_favorites(data):
        query = """
                INSERT INTO favorites (author_id,book_id)
                VALUES (%(author_id)s, %(book_id)s) 
                """
        connectToMySQL('books').query_db(query,data)

    @classmethod
    def delete(cls,data):
        pass

    @classmethod
    def update(cls,data):
        pass

