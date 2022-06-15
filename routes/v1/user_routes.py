from fastapi import APIRouter

from controllers import user_controllers
from middlewares.admin_check import admin_check
from middlewares.auth_check import auth_check

userroutes = APIRouter()
# userroutes.before_request(auth_check)
# userroutes.before_request(admin_check)

userroutes.get("/")(user_controllers.get_all)
userroutes.get("/{id}")(user_controllers.get_by_id)
userroutes.post("/")(user_controllers.create)
userroutes.put("/{id}")(user_controllers.update)
userroutes.delete("/{id}")(user_controllers.remove)
