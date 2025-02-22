from fastapi import APIRouter, Depends
from app.core.auth import verify_token
from app.models.stable_diffusion import stable_diffusion_model

router = APIRouter()


@router.post("/product-image")
async def generate_product_image(prompt: str, token_data: dict = Depends(verify_token)):
    """Generates product image using Stable Diffusion"""
    image_path = stable_diffusion_model.generate(prompt)
    return {"image_url": image_path}
