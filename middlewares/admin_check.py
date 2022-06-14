import os
import jwt
from flask import g, make_response, request

secret_key = os.environ.get('SECRET_KEY')


def admin_check():
    if g.role != 'admin':
        return make_response({'message': 'Cannot access this route, since the current user is not an admin.'}, 400)
