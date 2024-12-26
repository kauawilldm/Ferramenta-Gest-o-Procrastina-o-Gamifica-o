from fastapi import APIRouter

router = APIRouter()

tasks_data = []

@router.post("/tasks/")
def add_task(task: dict):
    tasks_data.append(task)
    return {"message": "Tarefa adicionada!", "task": task}

@router.get("/tasks/")
def list_tasks():
    return {"tasks": tasks_data}
