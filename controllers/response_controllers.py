import json

from bson import ObjectId
from helpers.utils import lookup, prune_fields, filter_deleted
from fastapi.responses import JSONResponse

from datetime import datetime

from models.response_model import Response

async def get_all():
    try:
        pipeline = [
            *lookup('tag:_id', 'tag_ids'),
            *filter_deleted(['title', 'content'], 'tag_ids'),
            *prune_fields(['title', 'content'], 'tag_ids', ['_id', 'tag']),
        ]  # for population of objects
        responses_raw = Response.objects().aggregate(pipeline)
        responses = json.loads(json.dumps(list(responses_raw), default=str))
        return JSONResponse(responses, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def get_by_id(id: str):
    try:
        pipeline = [
            *lookup('tag:_id', 'tag_ids'),
            *filter_deleted(['title', 'content'], 'tag_ids'),
            *prune_fields(['title', 'content'], 'tag_ids', ['_id', 'tag']),
        ]  # for population of objects
        responses_raw = Response.objects(id=id).aggregate(pipeline)
        responses = json.loads(json.dumps(list(responses_raw), default=str))
        response = responses[0] if responses else {}
        return JSONResponse(response, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def create():
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
        return JSONResponse(response, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def update(id: str):
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
        return JSONResponse(response, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def remove(id: str):
    try:
        # Response.objects(id=id).delete()
        # In very rare occasions, the database removes documents entirely
        # What one usually does is to update the document with {deleted:True}
        Response.objects(id=id).update(updated_at=datetime.utcnow,
                                       deleted_at=datetime.utcnow,
                                       deleted=True)

        return JSONResponse({'message': 'document successfully deleted'}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)