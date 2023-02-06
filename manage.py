import logging
import sqlalchemy
from fastapi import FastAPI


log = logging.getLogger("my-api")
FORMAT = "%(levelname)s:%(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

app = FastAPI()

#Include views
from views.users import users_api_router

app.include_router(users_api_router)

