from fastapi import APIRouter

from controllers import response_controllers
from middlewares.auth_check import auth_check

responseroutes = APIRouter(tags=["Response"])
# responseroutes.before_request(auth_check)

responseroutes.get("/", description="Get all responses")(response_controllers.get_all)
responseroutes.get("/{id}", description="Get one response")(response_controllers.get_by_id)
responseroutes.post("/", description="Create a new response")(response_controllers.create)
responseroutes.put("/{id}", description="Update one response")(response_controllers.update)
responseroutes.delete("/{id}", description="Delete one response")(response_controllers.remove)

