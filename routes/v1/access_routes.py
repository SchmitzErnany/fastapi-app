from fastapi import APIRouter

from controllers import access_controllers
from helpers.schemas import TokensSchema

accessroutes = APIRouter(tags=["Access"])

accessroutes.post("/login", description="Obtain access tokens", response_model=TokensSchema)(access_controllers.login)
accessroutes.post("/refresh", description="Refresh access tokens", response_model=TokensSchema)(access_controllers.refresh)
