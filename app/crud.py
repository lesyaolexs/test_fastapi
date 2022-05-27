from typing import List, Optional
from uuid import UUID

import sqlalchemy

from app.database import db
from app.models.user import User as modelsUser
from app.schemas.user import DBUser, PatchUser
from app.schemas.user import User as schemasUser


async def get_users(offset: int = 0, limit: int = 100) -> List[DBUser]:
    query = sqlalchemy.select(modelsUser).offset(offset).limit(limit)
    users = await db.fetch_all(query=query)
    return [DBUser.parse_obj(user) for user in users]


async def get_user(user_id: UUID) -> Optional[DBUser]:
    query = sqlalchemy.select(modelsUser).where(modelsUser.id == user_id)
    user = await db.fetch_one(query=query)
    if user:
        return DBUser.parse_obj(user)
    return None


async def create_user(user: schemasUser) -> DBUser:
    query = sqlalchemy.insert(modelsUser).values(
        first_name=user.first_name, last_name=user.last_name, birthday=user.birthday
    )
    last_record_id = await db.execute(query)
    return DBUser.parse_obj({**user.dict(), "id": last_record_id})


async def update_user(user_id: UUID, user: PatchUser) -> Optional[DBUser]:
    query = (
        sqlalchemy.update(modelsUser)
        .where(modelsUser.id == user_id)
        .values(
            first_name=user.first_name, last_name=user.last_name, birthday=user.birthday
        )
    )
    await db.execute(query)

    return await get_user(user_id)
