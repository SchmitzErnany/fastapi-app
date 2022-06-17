from typing import List
from fastapi import APIRouter, Depends

from controllers import tag_controllers
from helpers.schemas import DeleteMessageSchema, TagSavedSchema
from middlewares.auth_check import JWTBearer


tagroutes = APIRouter(tags=["Tag"], dependencies=[Depends(JWTBearer())])

tagroutes.get("/", description="Get all tags", response_model=List[TagSavedSchema])(tag_controllers.get_all)
tagroutes.get("/{id}", description="Get one tag", response_model=TagSavedSchema)(tag_controllers.get_by_id)
tagroutes.post("/", description="Create a new tag", response_model=TagSavedSchema)(tag_controllers.create)
tagroutes.put("/{id}", description="Update one tag", response_model=TagSavedSchema)(tag_controllers.update)
tagroutes.delete("/{id}", description="Delete one tag", response_model=DeleteMessageSchema)(tag_controllers.remove)
