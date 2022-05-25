from typing import List

from fastapi import FastAPI

from schemas.user import PatchUser, User

app = FastAPI()


@app.get("/")
def healthcheck() -> str:
    return "OK"


@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    ...


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str) -> User:
    ...


@app.post("/users", response_model=User)
async def create_user(user: User) -> User:
    ...


@app.patch("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: PatchUser) -> User:
    ...


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: str) -> User:
    ...
