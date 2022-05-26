from sqlalchemy.orm import Session

from app.models.user import User


def get_users(db: Session, offset: int = 0, limit: int = 100):
    return db.query(User).offset(offset).limit(limit).all()
