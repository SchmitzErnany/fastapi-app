from flask import Blueprint, g

from controllers import access_controllers
from middlewares.auth_check import auth_check

accessroutes = Blueprint('access', __name__)

accessroutes.post("/login")(access_controllers.login)
accessroutes.post("/refresh")(access_controllers.refresh)
