from fastapi import APIRouter, Depends

from controllers import response_controllers
from middlewares.auth_check import JWTBearer


responseroutes = APIRouter(tags=["Response"], dependencies=[Depends(JWTBearer())])

responseroutes.get("/", description="Get all responses")(response_controllers.get_all)
responseroutes.get("/{id}", description="Get one response")(response_controllers.get_by_id)
responseroutes.post("/", description="Create a new response")(response_controllers.create)
responseroutes.put("/{id}", description="Update one response")(response_controllers.update)
responseroutes.delete("/{id}", description="Delete one response")(response_controllers.remove)

