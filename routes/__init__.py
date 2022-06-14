from flask import Blueprint

from .v1 import v1_routes

all_routes = Blueprint('all_routes', __name__)
all_routes.register_blueprint(v1_routes, url_prefix='/api/services/v1')