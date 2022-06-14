from flask import Blueprint, g, render_template

from controllers import response_controllers
from middlewares.auth_check import auth_check

responseroutes = Blueprint('response', __name__)
# responseroutes.before_request(auth_check)

responseroutes.get("/")(response_controllers.get_all)
responseroutes.get("/<string:id>")(response_controllers.get_by_id)
responseroutes.post("/")(response_controllers.create)
responseroutes.put("/<string:id>")(response_controllers.update)
responseroutes.delete("/<string:id>")(response_controllers.remove)

