from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        ''' If user with specific name exists, return with error.
            If not, create that user according to the request data. '''
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "Username already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created."}, 201
