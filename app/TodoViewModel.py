from pydantic import BaseModel

class ToDoViewModel(BaseModel):

    Title :str 
    Completed :str
    EmailId :str

