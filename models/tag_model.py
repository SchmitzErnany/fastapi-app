from mongoengine import Document, StringField, DateTimeField, BooleanField
from datetime import datetime


class Tag(Document):
    tag = StringField(required=True, unique=True, min_length=1)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    deleted = BooleanField(default=False)
    deleted_at = DateTimeField(default=None)
