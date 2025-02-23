import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DJANGO_AUTH_URL: str = os.getenv("DJANGO_AUTH_URL")
    STACKGAN_MODEL_URL: str = os.getenv("STACKGAN_MODEL_URL")
    STABLE_DIFFUSION_MODEL_PATH = os.getenv("STABLE_DIFFUSION_MODEL_PATH")


settings = Settings()
