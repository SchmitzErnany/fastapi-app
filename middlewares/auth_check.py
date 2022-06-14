import os
import jwt
from flask import g, make_response, request

secret_key = os.environ.get('SECRET_KEY')


def auth_check():
    if 'Authorization' not in request.headers.keys():
        return make_response({'message': 'Token not found. Try again.'}, 400)

    auth = request.headers['Authorization']
    auth_split = auth.split(' ')
    if len(auth_split) == 1:
        token = auth_split[0]
    elif len(auth_split) == 2 and auth_split[0] == 'Bearer':
        token = auth_split[1]
    else:
        return make_response({'message': 'Token is not well formatted. Try again.'}, 400)

    if not token:
        return make_response({'message': 'Token is missing!'}, 400)

    # decoding the token and obtaining the corresponding user
    try:
        info = jwt.decode(token, key=secret_key)
        g.role = info['role']
    except:
        return make_response({'message': 'Token is invalid!'}, 400)
    
        

