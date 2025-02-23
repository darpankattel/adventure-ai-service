import requests
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def verify_token(token: str = Security(oauth2_scheme)):
    """Verifies token via Django API"""
    response = requests.get(settings.DJANGO_AUTH_URL, headers={
                            "Authorization": f"Bearer {token}"})
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid token")
    return response.json()  # Return user data from Django
