# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

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
        "endpoints": {
            "List tasks": "/tasks/",
            "Create task": "/tasks/",
            "Task detail": "/tasks/{id}/",
            "Update task": "/tasks/{id}/",
            "Delete task": "/tasks/{id}/"
        }
    }

@app.get("/tasks/", response_model=list[schemas.TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.patch("/tasks/{task_id}/", response_model=schemas.TaskOut)
def update_task(task_id: int, updates: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, updates)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task successfully deleted."}
