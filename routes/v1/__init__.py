from flask import Blueprint

from .response_routes import responseroutes
from .tag_routes import tagroutes
from .user_routes import userroutes
from .access_routes import accessroutes

v1_routes = Blueprint('v1_routes', __name__)
v1_routes.register_blueprint(responseroutes, url_prefix='/response')
v1_routes.register_blueprint(tagroutes, url_prefix='/tag')
v1_routes.register_blueprint(userroutes, url_prefix='/user')
v1_routes.register_blueprint(accessroutes, url_prefix='/access')