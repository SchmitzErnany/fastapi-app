from fastapi import APIRouter

from .v1 import v1_routes

all_routes = APIRouter()
all_routes.include_router(v1_routes, prefix='/api/services/v1')