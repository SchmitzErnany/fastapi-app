from typing import List
from fastapi import APIRouter, Depends

from controllers import response_controllers
from helpers.schemas import DeleteMessageSchema, ResponseSavedSchema
from middlewares.auth_check import JWTBearer


responseroutes = APIRouter(tags=["Response"], dependencies=[Depends(JWTBearer())])

responseroutes.get("/", description="Get all responses", response_model=List[ResponseSavedSchema])(response_controllers.get_all)
responseroutes.get("/{id}", description="Get one response", response_model=ResponseSavedSchema)(response_controllers.get_by_id)
responseroutes.post("/", description="Create a new response", response_model=ResponseSavedSchema)(response_controllers.create)
responseroutes.put("/{id}", description="Update one response", response_model=ResponseSavedSchema)(response_controllers.update)
responseroutes.delete("/{id}", description="Delete one response", response_model=DeleteMessageSchema)(response_controllers.remove)

