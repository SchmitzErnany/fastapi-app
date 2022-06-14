import json

from bson import ObjectId
from flask import jsonify, make_response, request, g
from helpers.utils import lookup, prune_fields, filter_deleted

from datetime import datetime

from models.response_model import Response


def get_all():
    try:
        pipeline = [
            *lookup('tag:_id', 'tag_ids'),
            *filter_deleted(['title', 'content'], 'tag_ids'),
            *prune_fields(['title', 'content'], 'tag_ids', ['_id', 'tag']),
        ]  # for population of objects
        responses_raw = Response.objects().aggregate(pipeline)
        responses = json.loads(json.dumps(list(responses_raw), default=str))
        return make_response(jsonify(responses), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def get_by_id(id):
    try:
        pipeline = [
            *lookup('tag:_id', 'tag_ids'),
            *filter_deleted(['title', 'content'], 'tag_ids'),
            *prune_fields(['title', 'content'], 'tag_ids', ['_id', 'tag']),
        ]  # for population of objects
        responses_raw = Response.objects(id=id).aggregate(pipeline)
        responses = json.loads(json.dumps(list(responses_raw), default=str))
        response = responses[0] if responses else {}
        return make_response(jsonify(response), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def create():
    print(request.json)
    try:
        response_saved_raw = Response(**request.json).save()
        response_saved_id = json.loads(
            response_saved_raw.to_json())['_id']['$oid']
        pipeline = [
            *lookup('tag:_id', 'tag_ids'),
            *filter_deleted(['title', 'content'], 'tag_ids'),
            *prune_fields(['title', 'content'], 'tag_ids', ['_id', 'tag']),
        ]  # for population of objects
        response_raw = Response.objects(
            id=response_saved_id).aggregate(pipeline)
        response = json.loads(json.dumps(list(response_raw), default=str))[0]
        return make_response(jsonify(response), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def update(id):
    try:
        if "tag_ids" in request.json.keys():
            request.json["tag_ids"] = map(ObjectId, request.json["tag_ids"])

        Response.objects(id=id).update(**request.json, 
                                       updated_at=datetime.utcnow)
        pipeline = [
            *lookup('tag:_id', 'tag_ids'),
            *filter_deleted(['title', 'content'], 'tag_ids'),
            *prune_fields(['title', 'content'], 'tag_ids', ['_id', 'tag']),
        ]  # for population of objects
        response_raw = Response.objects(id=id).aggregate(pipeline)
        response = json.loads(json.dumps(list(response_raw), default=str))[0]
        return make_response(jsonify(response), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)


def remove(id):
    try:
        # Response.objects(id=id).delete()
        # In very rare occasions, the database removes documents entirely
        # What one usually does is to update the document with {deleted:True}
        Response.objects(id=id).update(updated_at=datetime.utcnow,
                                       deleted_at=datetime.utcnow,
                                       deleted=True)

        return make_response({'message': 'document successfully deleted'}, 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)