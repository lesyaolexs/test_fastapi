from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas.user import DBUser, PatchUser, User

app = FastAPI()


@app.get("/")
def healthcheck() -> str:
    return "OK"


@app.get("/users", response_model=List[DBUser])
async def get_users(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[DBUser]:
    users = crud.get_users(db, offset=offset, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str, db: Session = Depends(get_db)) -> User:
    ...


@app.post("/users", response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)) -> User:
    ...


@app.patch("/users/{user_id}", response_model=User)
async def update_user(
    user_id: str, user: PatchUser, db: Session = Depends(get_db)
) -> User:
    ...


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: str, db: Session = Depends(get_db)) -> User:
    ...
