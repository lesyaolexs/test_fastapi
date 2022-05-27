from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException
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
    return await crud.get_users(offset=offset, limit=limit)


@app.get("/users/{user_id}", response_model=DBUser)
async def get_user(user_id: UUID) -> User:
    user = await crud.get_user(user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@app.post("/users", response_model=DBUser)
async def create_user(user: User) -> DBUser:
    return await crud.create_user(user)


@app.patch("/users/{user_id}", response_model=DBUser)
async def update_user(user_id: UUID, user: PatchUser) -> User:
    updated_user = await crud.update_user(user_id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_user


@app.delete("/users/{user_id}", response_model=DBUser)
async def delete_user(user_id: UUID) -> User:
    deleted_user = await crud.delete_user(user_id)

    if deleted_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_user
