
from pydantic import BaseModel, ConfigDict


class TodoCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TodoUpdate(TodoCreate):
    pass

class TodoResponse(TodoCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
