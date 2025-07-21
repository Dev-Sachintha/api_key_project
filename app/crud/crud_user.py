from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import generate_api_key


def get_user_by_username(db: Session, username: str):
    """Fetches a user by their username."""
    return db.query(User).filter(User.username == username).first()


def get_user_by_api_key(db: Session, api_key: str):
    """Fetches a user by their API key."""
    return db.query(User).filter(User.api_key == api_key).first()


def create_user(db: Session, username: str) -> User:
    """Creates a new user with a unique API key."""
    new_api_key = generate_api_key()

    db_user = User(username=username, api_key=new_api_key)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
