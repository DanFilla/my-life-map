import sqlalchemy
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://root:root@localhost/my_life_app"

engine = sqlalchemy.create_engine(
    DATABASE_URL
) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
