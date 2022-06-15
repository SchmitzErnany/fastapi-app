from fastapi import APIRouter

from .response_routes import responseroutes
from .tag_routes import tagroutes
from .user_routes import userroutes
from .access_routes import accessroutes

v1_routes = APIRouter()
v1_routes.include_router(responseroutes, prefix='/response')
v1_routes.include_router(tagroutes, prefix='/tag')
v1_routes.include_router(userroutes, prefix='/user')
v1_routes.include_router(accessroutes, prefix='/access')