from fastapi import FastAPI
from .api.v1.endpoints import users, analysis
from .database import Base, engine


# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Relationship AI Backend",
    description="Backend service for the Relationship AI app with API Key authentication.",
    version="1.0.0",
)

# Include routers from different endpoint files
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(analysis.router, prefix="/api/v1", tags=["AI Analysis"])


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Relationship AI API"}
