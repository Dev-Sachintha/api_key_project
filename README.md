# API Key Project

A sample project demonstrating how to build a secure API key system using Python, FastAPI, and SQLAlchemy.

## Project Structure

- `app/`: Main application source code.
  - `api/`: API endpoint definitions and dependencies.
  - `core/`: Core logic and security functions.
  - `crud/`: Database interaction logic (Create, Read, Update, Delete).
  - `models/`: SQLAlchemy database models.
  - `schemas/`: Pydantic data validation schemas.
  - `database.py`: Database session setup.
  - `main.py`: Main FastAPI app entry point.
- `requirements.txt`: Python package dependencies.

## Setup

1.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To run the development server:

```bash
uvicorn app.main:app --reload