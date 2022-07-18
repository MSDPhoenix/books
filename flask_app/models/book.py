from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.author import Author

class Book():
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        results = connectToMySQL('books').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_favorites(cls,data):
        query = '''
                SELECT * FROM books
                LEFT JOIN favorites ON books.id = favorites.book_id
                WHERE favorites.author_id = %(author_id)s;
                '''
        results = connectToMySQL('books').query_db(query,data)
        favorites = []
        for book in results:
            favorites.append(cls(book))
        return favorites

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM books WHERE id=%(book_id)s;'
        result = connectToMySQL('books').query_db(query,data)
        # print("result[0] = ",result[0])
        book = cls(result[0])
        book.favorites=Author.get_favorites(data)
        return book

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO books (title,num_of_pages)
                VALUES (%(title)s,%(num_of_pages)s)
                """
        return connectToMySQL('books').query_db(query,data)

    @classmethod
    def add_to_favorites(cls,data):
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

