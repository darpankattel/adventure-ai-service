import torch
from diffusers import StableDiffusionPipeline
from app.core.config import settings


class StableDiffusion:
    def __init__(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            settings.STABLE_DIFFUSION_MODEL_PATH)
        self.pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    def generate(self, prompt: str, type_: str, id: str):
        assert type_ in [
            "product", "background"], "Invalid type_, must be 'product' or 'background'"
        image = self.pipe(prompt).images[0]
        output_path = f"generated_images/{type_}_{id}.png"
        image.save(output_path)
        return output_path


stable_diffusion_model = StableDiffusion()
