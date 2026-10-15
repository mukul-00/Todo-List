
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import Base, engine, get_db
from models import Todo
from schemas import TodoCreate, TodoResponse

app = FastAPI(title="Todo API")

# Create database tables
Base.metadata.create_all(bind=engine)


# CREATE
@app.post("/todos/", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


# READ ALL
@app.get("/todos/", response_model=list[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)


# READ ONE
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


# UPDATE
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, data: TodoCreate, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id, data)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


# DELETE
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.delete_todo(db, todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted successfully"}
