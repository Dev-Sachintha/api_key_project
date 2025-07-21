# D:\tree\python\api_key_project\app\api\v1\endpoints\analysis.py

from fastapi import APIRouter, Depends
from app.api.v1.dependencies import get_current_user
from app.models.user import User as UserModel
from app.schemas.sentiment import (
    SentimentRequest,
    SentimentResponse,
)  # This import must match the class names in the file above

# Create a router to organize endpoints
router = APIRouter()


def _mock_sentiment_analysis(text: str) -> float:
    """
    A simple rule-based sentiment analysis function.
    This is where your custom AI logic would live.
    It returns a score between -1.0 and 1.0.
    """
    text_lower = text.lower()
    positive_words = [
        "love",
        "happy",
        "great",
        "excellent",
        "good",
        "amazing",
        "support",
        "appreciate",
    ]
    negative_words = [
        "hate",
        "sad",
        "terrible",
        "bad",
        "angry",
        "awful",
        "problem",
        "conflict",
    ]

    score = 0.0

    # Check for positive and negative keywords to adjust the score
    for word in positive_words:
        if word in text_lower:
            score += 0.5

    for word in negative_words:
        if word in text_lower:
            score -= 0.5

    # Clamp the score to ensure it stays within the -1.0 to 1.0 range
    return max(-1.0, min(1.0, score))


@router.post("/analysis/sentiment", response_model=SentimentResponse)
def perform_sentiment_analysis(
    request: SentimentRequest, current_user: UserModel = Depends(get_current_user)
):
    """
    Performs sentiment analysis on the provided text.
    This is a protected endpoint and requires a valid `api-key` in the header.

    - **Request Body**: A JSON object with a "text" key.
    - **Headers**: Requires a valid "api-key".
    - **Returns**: A JSON object with the calculated "sentiment_score".
    """
    # The `get_current_user` dependency has already validated the API key.
    # You can now use the `current_user` object for logging or other logic.
    print(
        f"Sentiment analysis requested by user: {current_user.username} (ID: {current_user.id})"
    )

    # Call the analysis function with the text from the request
    score = _mock_sentiment_analysis(request.text)

    # Return the result, which FastAPI will validate against the SentimentResponse schema
    return {"sentiment_score": score}
