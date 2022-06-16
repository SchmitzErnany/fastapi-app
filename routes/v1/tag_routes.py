from fastapi import APIRouter

from controllers import tag_controllers
from middlewares.auth_check import auth_check

tagroutes = APIRouter(tags=["Tag"])
# tagroutes.before_request(auth_check)

tagroutes.get("/", description="Get all tags")(tag_controllers.get_all)
tagroutes.get("/{id}", description="Get one tag")(tag_controllers.get_by_id)
tagroutes.post("/", description="Create a new tag")(tag_controllers.create)
tagroutes.put("/{id}", description="Update one tag")(tag_controllers.update)
tagroutes.delete("/{id}", description="Delete one tag")(tag_controllers.remove)
