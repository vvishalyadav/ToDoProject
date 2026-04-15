from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    Address:str
    Sports: str|list=None

