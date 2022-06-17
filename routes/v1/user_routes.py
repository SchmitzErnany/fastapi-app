from typing import List
from fastapi import APIRouter, Depends

from controllers import user_controllers
from helpers.schemas import DeleteMessageSchema, UserSavedSchema
from middlewares.auth_check import JWTBearer

userroutes = APIRouter(tags=["User"], dependencies=[Depends(JWTBearer(admin_check=True))])

userroutes.get("/", description="Get all users", response_model=List[UserSavedSchema])(user_controllers.get_all)
userroutes.get("/{id}", description="Get one user", response_model=UserSavedSchema)(user_controllers.get_by_id)
userroutes.post("/", description="Create a new user", response_model=UserSavedSchema)(user_controllers.create)
userroutes.put("/{id}", description="Update one user", response_model=UserSavedSchema)(user_controllers.update)
userroutes.delete("/{id}", description="Delete one user", response_model=DeleteMessageSchema)(user_controllers.remove)
