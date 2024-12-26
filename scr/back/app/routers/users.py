from fastapi import APIRouter

router = APIRouter()

users_data = {}

@router.put("/users/{username}/score/")
def update_score(username: str, score: int):
    if username not in users_data:
        users_data[username] = {"score": 0}
    users_data[username]["score"] += score
    return {"username": username, "new_score": users_data[username]["score"]}
