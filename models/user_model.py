from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True, regex="^(user|admin)$", default='user')
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
