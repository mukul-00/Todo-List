
from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoCreate, TodoUpdate


# CREATE
def create_todo(db: Session, todo: TodoCreate):
    new_todo = Todo(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# READ ALL
def get_todos(db: Session):
    return db.query(Todo).all()


# READ ONE
def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


# UPDATE
def update_todo(db: Session, todo_id: int, data: TodoUpdate):
    todo = get_todo(db, todo_id)

    if todo is None:
        return None

    todo.title = data.title
    todo.description = data.description
    todo.completed = data.completed

    db.commit()
    db.refresh(todo)
    return todo


# DELETE
def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)

    if todo is None:
        return None

    db.delete(todo)
    db.commit()
    return todo
