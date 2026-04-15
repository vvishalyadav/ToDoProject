from  sqlalchemy import Column,Integer,String
from app.database.connection import Base
from sqlalchemy.orm import relationship
# from app.models.ToDo import ToDo

class User(Base):
    __tablename__ ="users"
    
    id= Column(Integer,primary_key=True,index=True)
    EmailId =Column(String,nullable=False,unique=True)
    name=Column(String,index=True)

    todos = relationship("ToDo",back_populates="users")
  #  age=Column(Integer)
