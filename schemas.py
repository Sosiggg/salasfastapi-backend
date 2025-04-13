from pydantic import BaseModel

class TaskBase(BaseModel):
    text: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    text: str | None = None
    completed: bool | None = None

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True
