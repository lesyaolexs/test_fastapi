from typing import List
from uuid import UUID

from fastapi import FastAPI
from pydantic import NonNegativeInt

from app import crud
from app.database import db
from app.schemas.user import DBUser, PatchUser, User

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
def healthcheck() -> str:
    return "OK"


@app.get("/users", response_model=List[DBUser])
async def get_users(
    offset: NonNegativeInt = 0, limit: NonNegativeInt = 100
) -> List[DBUser]:
    users = await crud.get_users(offset=offset, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: UUID) -> User:
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
