from fastapi import APIRouter

from controllers import tag_controllers
from middlewares.auth_check import auth_check

tagroutes = APIRouter()
# tagroutes.before_request(auth_check)

tagroutes.get("/")(tag_controllers.get_all)
tagroutes.get("/{id}")(tag_controllers.get_by_id)
tagroutes.post("/")(tag_controllers.create)
tagroutes.put("/{id}")(tag_controllers.update)
tagroutes.delete("/{id}")(tag_controllers.remove)
