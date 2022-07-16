from flask_app.config.mysqlconnection import connectToMySQL

class Author():
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_one(cls,data):
        pass

    @classmethod
    def save(cls,data):
        pass

    @classmethod
    def delete(cls,data):
        pass

    @classmethod
    def update(cls,data):
        pass

