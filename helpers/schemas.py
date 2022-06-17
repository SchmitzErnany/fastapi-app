from typing import List
from pydantic import BaseModel, Field

###################
### OUTPUTS
###################
class DeleteMessageSchema(BaseModel):
    message: str = Field()

class TagSavedSchema(BaseModel):
    id: str = Field(alias='_id')
    tag: str = Field()
    # created_at: str = Field()
    # deleted: bool = Field()
    # deleted_at: str = Field()
    # updated_at: str = Field()

class ResponseSavedSchema(BaseModel):
    id: str = Field(alias='_id')
    content: str = Field()
    tag_ids: List[TagSavedSchema]
    title: str = Field()
    # created_at: str = Field()
    # deleted: bool = Field()
    # deleted_at: str = Field()
    # updated_at: str = Field()

class UserSavedSchema(BaseModel):
    id: str = Field(alias='_id')
    role: str = Field()
    username: str = Field()
    password: str = Field()
    # created_at: str = Field()
    # deleted: bool = Field()
    # deleted_at: str = Field()
    # updated_at: str = Field()

class TokensSchema(BaseModel):
    access_token: str = Field()
    refresh_token: str = Field()

###################
### INPUTS
###################

class TagSchema(BaseModel):
    tag: str = Field()

class ResponseSchema(BaseModel):
    content: str = Field()
    tag_ids: list = Field()
    title: str = Field()

class UserSchema(BaseModel):
    role: str = Field()
    username: str = Field()
    password: str = Field()

class CredentialsSchema(BaseModel):
    username: str = Field()
    password: str = Field()

class RefreshSchema(BaseModel):
    refresh_token: str = Field()



