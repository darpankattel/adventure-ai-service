from fastapi import APIRouter, Depends
from app.core.auth import verify_token
from app.models.stable_diffusion import stable_diffusion_model
from datetime import datetime

router = APIRouter()


@router.get("/background")
# token_data: dict = Depends(verify_token)
async def generate_background_image(prompt: str):
    """Generates background image using StackGAN"""
    image_path = stable_diffusion_model.generate(
        prompt, "background", datetime.now().strftime("%Y%m%d%H%M%S"))
    return {"image_url": image_path}
