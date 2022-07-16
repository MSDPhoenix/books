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

