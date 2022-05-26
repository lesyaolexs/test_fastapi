from sqlalchemy import Column, Date, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True), server_default=func.uuid_generate_v4(), primary_key=True
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthday = Column(Date)
