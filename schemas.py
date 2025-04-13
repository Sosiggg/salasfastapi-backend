from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    text: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    text: Optional[str] = None
    completed: Optional[bool] = None

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True
