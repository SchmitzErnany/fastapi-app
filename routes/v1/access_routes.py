from fastapi import APIRouter

from controllers import access_controllers
from middlewares.auth_check import auth_check

accessroutes = APIRouter()

accessroutes.post("/login")(access_controllers.login)
accessroutes.post("/refresh")(access_controllers.refresh)
