from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from pydantic import BaseModel

router = APIRouter()

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@router.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = models.Todo(title=todo.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Not found")
    if todo.title is not None:
        db_todo.title = todo.title
    if todo.done is not None:
        db_todo.done = todo.done
    db.commit()
    return db_todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(db_todo)
    db.commit()
    return {"ok": True}