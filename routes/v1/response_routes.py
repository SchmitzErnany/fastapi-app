from fastapi import APIRouter

from controllers import response_controllers
from middlewares.auth_check import auth_check

responseroutes = APIRouter()
# responseroutes.before_request(auth_check)

responseroutes.get("/")(response_controllers.get_all)
responseroutes.get("/{id}")(response_controllers.get_by_id)
responseroutes.post("/")(response_controllers.create)
responseroutes.put("/{id}")(response_controllers.update)
responseroutes.delete("/{id}")(response_controllers.remove)

