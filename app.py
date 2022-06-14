from fastapi import FastAPI
from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv

from routes import all_routes
from databases.mongodb import Mongodb
from helpers.errors import not_found, bad_request, server_error
from swagger_config import swagger_config

load_dotenv()
connection = Mongodb().create_connection()

app = FastAPI()

# app = Flask(__name__)
# app.register_blueprint(all_routes)

# Swagger(app, config=swagger_config, template_file='swagger.json')

# app.errorhandler(404)(not_found)
# app.errorhandler(400)(bad_request)
# app.errorhandler(500)(server_error)

# if __name__ == '__main__':
#     app.run(debug=True)

async def root():
    return {"message": "Hello World"}

app.get("/")(root)


