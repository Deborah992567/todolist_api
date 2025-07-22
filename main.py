from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

todolists = {
    1: {"title": "get the car fixed", "description": "wuse2location on monday", "due_date": str(date.today()), "done": True},
    2: {"title": "go to read books", "description": "library", "due_date": "wednesday", "done": False}
}

class Todo(BaseModel):
    id: int
    title: str
    description: str
    due_date: str
    done: bool

@app.get("/get-todolist/")
def read_todo():
    return todolists

@app.get("/get-todolist/{todo_id}/")
def get_todolist(todo_id: int = Path(..., description="get your todolist by id")):
    if todo_id in todolists:
        return todolists[todo_id]
    raise HTTPException(status_code=809, detail="not found sorry")

@app.get("/get-todolist-by-search")
def search_todolist(
    title: Optional[str] = Query(None, description="search by title"),
    description: Optional[str] = Query(None, description="search by description")
):
    results = {}
    for todo_id, todolist in todolists.items():
        if title and title.lower() in todolist["title"].lower():
            results[todo_id] = todolist
        elif description and description.lower() in todolist["description"].lower():
            results[todo_id] = todolist
    if not results:
        raise HTTPException(status_code=809, detail="not found sorry")
    return results

@app.post("/todos/{todo_id}")
def create_todo(todo: Todo, todo_id: int = Path(..., description="id of the todo item")):
    if todo_id in todolists:
        raise HTTPException(status_code=409, detail="todo item already exists")
    todolists[todo_id] = todo.dict()
    return todolists[todo_id]

@app.put("/todos/{todo_id}")
def update_todo(todo: Todo, todo_id: int = Path(..., description="update the todo item using id number")):
    if todo_id not in todolists:
        raise HTTPException(status_code=409, detail="todo item not found")
    todolists[todo_id] = todo.dict()
    return todolists[todo_id]

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int = Path(..., description="delete your todolist by id")):
    if todo_id not in todolists:
        raise HTTPException(status_code=809, detail="not found sorry")
    deleted = todolists.pop(todo_id)
    return {"message": f"todo {todo_id} deleted successfully", "deleted": deleted}
