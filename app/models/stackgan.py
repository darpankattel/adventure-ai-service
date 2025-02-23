from transformers import pipeline
from app.core.config import settings


class StackGAN:
    def __init__(self):
        self.pipe = pipeline(
            "text-to-image", model=settings.STACKGAN_MODEL_URL)

    def generate(self, prompt: str):
        image = self.pipe(prompt)[0]
        output_path = f"generated_images/background_{hash(prompt)}.png"
        image.save(output_path)
        return output_path  # Return local image URL


stackgan_model = StackGAN()
