from datetime import date
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    birthday: Optional[date]


class PatchUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[date]
