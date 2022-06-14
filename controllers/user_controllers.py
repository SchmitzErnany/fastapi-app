import json
from datetime import datetime
from flask import jsonify, make_response, request, g
from werkzeug.security import generate_password_hash
from helpers.utils import hide_password

from models.user_model import User


def get_all():
    try:
        pipeline = []
        users_raw = User.objects().aggregate(pipeline)
        users = json.loads(json.dumps(list(users_raw), default=str))
        users = list(map(hide_password, users))
        return make_response(jsonify(users), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def get_by_id(id):
    try:
        pipeline = []
        users_raw = User.objects(id=id).aggregate(pipeline)
        users = json.loads(json.dumps(list(users_raw), default=str))
        user = users[0] if users else {}
        user = hide_password(user)
        return make_response(jsonify(user), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def create():
    try:
        username = request.json['username']
        password_hash = generate_password_hash(request.json['password'])
        role = request.json['role']
        credentials = {
            'username': username,
            'password': password_hash,
            'role': role
        }

        user_saved = User(**credentials).save()
        user_saved_id = json.loads(user_saved.to_json())['_id']['$oid']
        pipeline = []  # for population of objects
        user_raw = User.objects(id=user_saved_id).aggregate(pipeline)
        user = json.loads(json.dumps(list(user_raw), default=str))[0]
        user = hide_password(user)
        return make_response(jsonify(user), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def update(id):
    try:
        User.objects(id=id).update(**request.json, updated_at=datetime.utcnow)
        pipeline = []  # for population of objects
        user_raw = User.objects(id=id).aggregate(pipeline)
        user = json.loads(json.dumps(list(user_raw), default=str))[0]
        user = hide_password(user)
        return make_response(jsonify(user), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def remove(id):
    try:
        # Tag.objects(id=id).delete()
        # In very rare occasions, the database removes documents entirely
        # What one usually does is to update the document with {deleted:True}
        User.objects(id=id).update(updated_at=datetime.utcnow,
                                   deleted_at=datetime.utcnow,
                                   deleted=True)

        return make_response({'message': 'document successfully deleted'}, 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)