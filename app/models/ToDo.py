from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from app.database.connection import Base
from sqlalchemy.orm import relationship
# from app.models.Users import User


class ToDo(Base):
    __tablename__ ="todos"
    id = Column(Integer,primary_key=True,index=True)
    Title = Column(String)
    Completed = Column(String, default=False)
    EmailId =Column(String,ForeignKey("users.EmailId"))

    users = relationship("User",back_populates="todos")

