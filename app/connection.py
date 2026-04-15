from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

Database_URL = "postgresql://postgres:Raosahab%4012@localhost:5432/TO_DO"

engine =  create_engine(Database_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()



