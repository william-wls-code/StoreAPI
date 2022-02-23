from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        ''' Return the store in json if it exists.
            If not, return an error. '''
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        ''' If store with specific name exists, return with error.
            If not, create that store. '''
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        ''' Delete store with specific name.
            Return error if that store does not exist.'''
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'message': "Store with name '{}' not found.".format(name)}, 404


class StoreList(Resource):
    def get(self):
        ''' Return a list of store in json from the stores table.
            Since it is a query, query.add() is used. '''
        return {'stores': [store.json() for store in StoreModel.query.all()]}
