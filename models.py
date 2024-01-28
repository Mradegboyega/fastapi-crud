from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="id")
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
