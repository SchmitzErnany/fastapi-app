from fastapi import APIRouter

from controllers import access_controllers
from middlewares.auth_check import auth_check

accessroutes = APIRouter(tags=["Access"])

accessroutes.post("/login", description="Obtain access tokens")(access_controllers.login)
accessroutes.post("/refresh", description="Refresh access tokens")(access_controllers.refresh)
