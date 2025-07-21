from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.schemas.user import User as UserSchema
from app.api.v1.dependencies import get_db

router = APIRouter()


@router.post("/users/register", response_model=UserSchema)
def register_new_user(username: str, db: Session = Depends(get_db)):
    """
    Registers a new user and generates a unique API key for them.
    - **username**: The desired username. Must be unique.
    """
    db_user = crud_user.get_user_by_username(db, username=username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return crud_user.create_user(db=db, username=username)
