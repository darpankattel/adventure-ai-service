from fastapi import FastAPI
from .api.endpoints import background, product_image
import os
os.environ["HF_HOME"] = "/app/cache"
os.environ["XDG_CACHE_HOME"] = "/app/cache"

app = FastAPI(title="AdVenture AI Microservice")

app.include_router(background.router, tags=["Background"])
app.include_router(product_image.router, tags=["Product Image"])


@app.get("/")
async def root():
    return {"message": "AI Image Generation Service is running!"}
