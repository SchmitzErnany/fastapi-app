from fastapi import APIRouter, Depends

from controllers import user_controllers
from middlewares.auth_check import JWTBearer

userroutes = APIRouter(tags=["User"], dependencies=[Depends(JWTBearer(admin_check=True))])

userroutes.get("/", description="Get all users")(user_controllers.get_all)
userroutes.get("/{id}", description="Get one user")(user_controllers.get_by_id)
userroutes.post("/", description="Create a new user")(user_controllers.create)
userroutes.put("/{id}", description="Update one user")(user_controllers.update)
userroutes.delete("/{id}", description="Delete one user")(user_controllers.remove)
