from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Access(Document):
    username = StringField(required=True)
    role = StringField(required=True, regex="^(user|admin)$", default='user')
    refresh_token = StringField()
    expiration_date = DateTimeField(default=datetime.utcnow)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    