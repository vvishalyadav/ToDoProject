from app.routes import users
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.Users import User
from app.models.ToDo import ToDo
from app.database.connection import engine,SessionLocal,Base
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.TodoViewModel import ToDoViewModel
from fastapi.responses import JSONResponse
# from app.schemas.UserViewModel import User
from fastapi import Form

# if __name__ =="__main__":
#     print(__name__)

app = FastAPI()

origins = [
    "http://localhost:3000",   # React / frontend
    "http://127.0.0.1:5500",  # Live Server
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router,prefix="/api/users",tags=["Users"])

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return "Amit"


@app.get("/users/names")
async def roottt():
    return ["vishal","Naman","Kartik"]

@app.get("/AllUsers")
async def getAllUsers( db:Session =Depends(get_db)):
    users = db.query(User).all()
    return users

@app.post("/user")
async def createUser(EmailId:str=Form(...),name:str=Form(...),db:Session=Depends(get_db)):

    user = User()
    user.name = name
    user.EmailId = EmailId
    
    db.add(user)
    db.commit()

    return {"redirect_to": f"/ToDo.html?name={user.name}&EmailId={user.EmailId}"}

@app.post("/api/ToDo")
async def create_Todo(todoView:ToDoViewModel,db:Session= Depends(get_db)):
    todo = ToDo(**todoView.model_dump())
    
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return {"id":todo.id} 

@app.put("/api/updateToDo")
async def updateToDo(status:str=Form(...),taskId:int=Form(...),db:Session=Depends(get_db)):
   todo = todo = db.query(ToDo).filter(ToDo.id == taskId).first()   
   if todo is not None:
          todo.Completed = status
          db.commit()
   return JSONResponse(status_code=200,content={"message":"task updated successfully"})

@app.delete("/api/deleteToDo")
async def deleteTodo(id:int=Form(...),db:Session=Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id==id).first()
    db.delete(todo)
    db.commit()
    return JSONResponse(status_code=204,content={"message":"task deleted successfully"})


@app.get("/api/AllToDo")
async def GetAll(EmailId:str,db:Session=Depends(get_db)):
   return db.query(ToDo).filter(ToDo.EmailId == EmailId).all() 


@app.get("/api/InProgressToDo")
async def InProgress(EmailId:str,db:Session=Depends(get_db)):
    return db.query(ToDo).filter(ToDo.EmailId == EmailId,ToDo.Completed=="Pending").all()


@app.put("/api/FinishAllToDo")
async def FinishAll(EmailId:str,db:Session=Depends(get_db)):
    db.query(ToDo).filter(ToDo.EmailId == EmailId).update({"Completed": "Completed"})
    db.commit()
    
    return db.query(ToDo).filter(ToDo.EmailId==EmailId).all()


@app.delete("/api/ClearAllToDo")
async def ClearAllTodo(EmailId:str,db:Session=Depends(get_db)):
    db.query(ToDo).filter(ToDo.EmailId == EmailId).delete(synchronize_session=False)
    db.commit()
    return {"message": "All todos deleted successfully"}


