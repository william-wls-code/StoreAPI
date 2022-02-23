from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    ''' Look for the username, if that user exists and the password is correct, return the user. '''
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    ''' Extract the user id from the payload. Then retrieve the specific user with the extracted user id. '''
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
