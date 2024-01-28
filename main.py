from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, status
from typing import List

from fastapi.responses import JSONResponse
from models import User, Gender, Role

app = FastAPI()

# Sample data
db: List[User] = [
    User(
        id=uuid4(),
        first_name="michelle",
        last_name="Ademola",
        middle_name=None,
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="toyin",
        last_name="Agbeniga",
        middle_name=None,
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Adegboyega",
        last_name="Ademola",
        middle_name=None,
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    """
    Root endpoint to greet the community.
    """
    return {"Hello": "community"}

@app.get("/api/v1/users")
async def fetch_users():
    """
    Endpoint to retrieve the list of users.
    """
    return db

@app.post("/api/v1/users")
async def add_users(user: User):
    """
    Endpoint to add a new user to the list.
    """
    user.id = uuid4()  # Generate a new ID
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}", response_model=dict)
async def delete_users(user_id: UUID):
    """
    Endpoint to delete a user by ID.
    """
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    # If user not found, raise a 404 error
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {user_id} not found")
