import json
import os
import secrets
import jwt
from flask import jsonify, make_response, request, g
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from dateutil.parser import parse

from models.access_model import Access

secret_key = os.environ.get('SECRET_KEY')
from models.user_model import User


def login():
    try:
        username = request.json['username']
        password = request.json['password']

        # checking if the user matches some user in the database
        database_users_raw = User.objects(username=username).aggregate([])
        database_users = json.loads(json.dumps(list(database_users_raw), default=str))
        database_user = database_users[0] if database_users_raw else None
        if not database_user:
            return make_response({'message': 'User not found!'}, 400)

        # checking if the password matches the user password in the database
        if not check_password_hash(database_user['password'], password):
            # if the password does not match the user password in the database
            return make_response({'message': 'Please check your name and password and try again.'}, 400)
        
        access_token = jwt.encode(
            {
                'username': database_user['username'],
                'role': database_user['role'],
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, secret_key)
        refresh_token = secrets.token_hex(nbytes=32)
        entry = {
            'username': database_user['username'],
            'role': database_user['role'],
            'expiration_date': datetime.utcnow() + timedelta(minutes=45),
            'refresh_token': refresh_token
        }

        updates = Access.objects(username=database_user['username']).update(**entry, updated_at=datetime.utcnow)
        if not updates:
            Access(**entry).save()

        return make_response({
            'access_token': access_token.decode('utf-8'),
            'refresh_token': refresh_token
        })
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)  


def refresh():
    try:
        refresh_token = request.json['refresh_token']

        database_accesses_raw = Access.objects(refresh_token=refresh_token).aggregate([])
        database_accesses = json.loads(json.dumps(list(database_accesses_raw), default=str))
        database_access = database_accesses[0] if database_accesses else None
        if not database_access:
            return make_response({'message': 'Token not found!'}, 400)
        if parse(database_access['expiration_date']) < datetime.utcnow():
            return make_response(
                {'message': 'Token expired! Please log in again.'}, 400)

        new_access_token = jwt.encode(
            {
                'username': database_access['username'],
                'role': database_access['role'],
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, secret_key)
        new_refresh_token = secrets.token_hex(nbytes=32)
        entry = {
            'username': database_access['username'],
            'role': database_access['role'],
            'expiration_date': datetime.utcnow() + timedelta(minutes=30),
            'refresh_token': new_refresh_token
        }

        updates = Access.objects(username=database_access['username']).update(**entry, updated_at=datetime.utcnow)
        if not updates:
            Access(**entry).save()

        return make_response({
            'access_token': new_access_token.decode('utf-8'),
            'refresh_token': new_refresh_token
        })
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)
