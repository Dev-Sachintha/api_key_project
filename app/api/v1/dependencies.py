from fastapi import Depends, HTTPException, Header, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import crud_user
from app.models.user import User


def get_db():
    """Dependency to create and close a database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    api_key: str = Header(..., description="The user's unique API key."),
    db: Session = Depends(get_db),
) -> User:
    """Dependency to validate the API key and return the associated user."""
    user = crud_user.get_user_by_api_key(db, api_key=api_key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key or user does not exist",
        )
    return user
