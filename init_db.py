from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://arsen:2431@localhost:5432/finance"

# Creating an engine object for working with Data Base
engine = create_engine(DATABASE_URL)

# Creating SessionLocal object for working with Data Base sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating Base object for using in models
Base = declarative_base()
