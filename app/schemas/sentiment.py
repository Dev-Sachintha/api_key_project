# D:\tree\python\api_key_project\app\schemas\sentiment.py

from pydantic import BaseModel


# --- Request Schema ---
# This class defines the structure of the JSON body that the client must send.
# It expects a JSON object like: {"text": "some message"}
class SentimentRequest(BaseModel):
    text: str


# --- Response Schema ---
# This class defines the structure of the JSON body that the server will send back.
# It will be a JSON object like: {"sentiment_score": 0.5}
class SentimentResponse(BaseModel):
    sentiment_score: float
