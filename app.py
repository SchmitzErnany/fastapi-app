from multiprocessing import freeze_support
from fastapi import FastAPI
from flasgger import Swagger
from dotenv import load_dotenv
import uvicorn

from routes import all_routes
from databases.mongodb import Mongodb
from helpers.errors import not_found, bad_request, server_error
from swagger_config import swagger_config

load_dotenv()
connection = Mongodb().create_connection()

app = FastAPI()
app.include_router(all_routes)

app.exception_handler(404)(not_found)
app.exception_handler(400)(bad_request)
app.exception_handler(500)(server_error)


# Swagger(app, config=swagger_config, template_file='swagger.json')

def run():
    uvicorn.run(app="app:app", host="0.0.0.0", port=8000, reload=True)