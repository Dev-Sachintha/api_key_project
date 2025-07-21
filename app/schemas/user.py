from pydantic import BaseModel


# Schema for returning user data, including the API key
class User(BaseModel):
    username: str
    api_key: str

    class Config:
        from_attributes = True  # Replaces orm_mode = True in Pydantic v2
