import secrets


def generate_api_key(length: int = 32) -> str:
    """
    Generates a secure, URL-safe random token.
    Default length is 32, which results in a 64-character hex string.
    """
    return secrets.token_hex(length)
