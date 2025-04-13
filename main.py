from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to the Salas' To-Do List API!",
        "documentation": "You can access the API documentation at /docs.",
        "endpoints": {
            "List all tasks": "/tasks/list/",
            "Create new task": "/tasks/create/",
            "Get task by ID": "/tasks/detail/{task_id}/",
            "Update task by ID": "/tasks/update/{task_id}/",
            "Delete task by ID": "/tasks/delete/{task_id}/"
        }
    }

@app.get("/tasks/list/", response_model=list[schemas.TaskOut], tags=["Tasks"])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/tasks/create/", response_model=schemas.TaskOut, tags=["Tasks"])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/detail/{task_id}/", response_model=schemas.TaskOut, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.patch("/tasks/update/{task_id}/", response_model=schemas.TaskOut, tags=["Tasks"])
def update_task(task_id: int, updates: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, updates)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/delete/{task_id}/", tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task successfully deleted."}

origins = [
    "http://localhost:3000", 
    "https://salastodolistfastapi.netlify.app/", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)
