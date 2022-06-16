import json
from flask import request

from datetime import datetime
from helpers.utils import prune_fields_tag, filter_deleted_tag

from models.tag_model import Tag
from fastapi.responses import JSONResponse


async def get_all():
    try:
        pipeline = [
            *filter_deleted_tag(),
            *prune_fields_tag(),
        ]
        tags_raw = Tag.objects().aggregate(pipeline)
        tags = json.loads(json.dumps(list(tags_raw), default=str))
        return JSONResponse(tags, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def get_by_id(id: str):
    try:
        pipeline = [
            *filter_deleted_tag(),
            *prune_fields_tag(),
        ]
        tags_raw = Tag.objects(id=id).aggregate(pipeline)
        tags = json.loads(json.dumps(list(tags_raw), default=str))
        tag = tags[0] if tags else {}
        return JSONResponse(tag, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def create():
    try:
        tag_saved_raw = Tag(**request.json).save()
        tag_saved_id = json.loads(tag_saved_raw.to_json())['_id']['$oid']
        pipeline = [
            *filter_deleted_tag(),
            *prune_fields_tag(),
        ]  # for population of objects
        tag_raw = Tag.objects(id=tag_saved_id).aggregate(pipeline)
        tag = json.loads(json.dumps(list(tag_raw), default=str))[0]
        return JSONResponse(tag, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def update(id: str):
    try:
        Tag.objects(id=id).update(**request.json, updated_at=datetime.utcnow)
        pipeline = [
            *filter_deleted_tag(),
            *prune_fields_tag(),
        ]  # for population of objects
        tag_raw = Tag.objects(id=id).aggregate(pipeline)
        tag = json.loads(json.dumps(list(tag_raw), default=str))[0]
        return JSONResponse(tag, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)


async def remove(id: str):
    try:
        # Tag.objects(id=id).delete()
        # In very rare occasions, the database removes documents entirely
        # What one usually does is to update the document with {deleted:True}
        Tag.objects(id=id).update(updated_at=datetime.utcnow,
                                  deleted_at=datetime.utcnow,
                                  deleted=True)

        return JSONResponse({'message': 'document successfully deleted'}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": str(err)}, status_code=400)