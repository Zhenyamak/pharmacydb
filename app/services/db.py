from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.lib.config import config


engine = create_engine(config['database']['uri'])

Session = sessionmaker(bind=engine)

session = Session()
