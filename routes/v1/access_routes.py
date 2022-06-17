from fastapi import APIRouter

from controllers import access_controllers

accessroutes = APIRouter(tags=["Access"])

accessroutes.post("/login", description="Obtain access tokens")(access_controllers.login)
accessroutes.post("/refresh", description="Refresh access tokens")(access_controllers.refresh)
