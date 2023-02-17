import logging
import sqlalchemy
from fastapi import FastAPI

from libs.logger import init_logger

init_logger(logging.DEBUG)

app = FastAPI()

# Include views
from views.users import users_api_router
from views.pins import pins_api_router

app.include_router(users_api_router)
app.include_router(pins_api_router)
