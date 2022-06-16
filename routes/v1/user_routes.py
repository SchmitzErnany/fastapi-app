from fastapi import APIRouter

from controllers import user_controllers
from middlewares.admin_check import admin_check
from middlewares.auth_check import auth_check

userroutes = APIRouter(tags=["User"])
# userroutes.before_request(auth_check)
# userroutes.before_request(admin_check)

userroutes.get("/", description="Get all users")(user_controllers.get_all)
userroutes.get("/{id}", description="Get one user")(user_controllers.get_by_id)
userroutes.post("/", description="Create a new user")(user_controllers.create)
userroutes.put("/{id}", description="Update one user")(user_controllers.update)
userroutes.delete("/{id}", description="Delete one user")(user_controllers.remove)
