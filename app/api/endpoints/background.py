from fastapi import APIRouter, Depends
from app.core.auth import verify_token
from app.models.stackgan import stackgan_model

router = APIRouter()


@router.post("/background")
async def generate_background_image(prompt: str, token_data: dict = Depends(verify_token)):
    """Generates background image using StackGAN"""
    image_path = stackgan_model.generate(prompt)
    return {"image_url": image_path}
