from db import db


class StoreModel(db.Model):
    # StoreModel is mapped in the database with table name 'stores'
    __tablename__ = 'stores'

    # Attributes of the table
    # id -- Int (Primary Key)
    # name -- String
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    # Use lazy='dynamic' such that self.items is not a list
    # It is a query builder that can look into the items table
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        ''' Return the StoreModel object as json '''
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()]
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
