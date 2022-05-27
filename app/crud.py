from uuid import UUID

import sqlalchemy

from app.database import db
from app.models.user import User


async def get_users(offset: int = 0, limit: int = 100):
    query = sqlalchemy.select(User).offset(offset).limit(limit)
    return await db.fetch_all(query=query)


async def get_user(user_id: UUID):
    query = sqlalchemy.select(User).where(User.id == user_id)
    return await db.fetch_one(query=query)
