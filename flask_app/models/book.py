from flask_app.config.mysqlconnection import connectToMySQL

class Book():
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        results = connectToMySQL('books').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_one(cls,data):
        pass

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO books (title,num_of_pages)
                VALUES (%(title)s,%(num_of_pages)s)
                """
        return connectToMySQL('books').query_db(query,data)

    @classmethod
    def delete(cls,data):
        pass

    @classmethod
    def update(cls,data):
        pass

