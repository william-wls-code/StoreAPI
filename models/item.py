from db import db


class ItemModel(db.Model):
    # ItemModel is mapped in the database with table name 'items'
    __tablename__ = 'items'

    # Attributes of the table
    # id -- Int (Primary Key)
    # username -- String
    # price -- Float
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        ''' SELECT * FROM items WHERE name=name LIMIT 1 '''
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        ''' Save the ItemModel object to the database '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' Delete the ItemModel object from the database '''
        db.session.delete(self)
        db.session.commit()
