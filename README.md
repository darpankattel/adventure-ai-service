---
title: StackGAN
emoji: 🐳
colorFrom: purple
colorTo: gray
sdk: docker
app_port: 7860
app_file: main.py
pinned: false
license: mit
short_description: For background generation
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# AdVenture AI Service

AdVenture AI Service is a FastAPI-based microservice for generating AI-generated images. It provides two endpoints for generating **background** and **product images** using StackGAN and Stable Diffusion, respectively.

## Features
- **User Authentication**: Authenticates users via a Django API before processing requests.
- **StackGAN for Background Images**: Generates realistic background images from text prompts.
- **Stable Diffusion for Product Images**: Creates high-quality product images from text descriptions.
- **Hugging Face Integration**: Uses pre-trained models from Hugging Face for seamless AI image generation.

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/adventure-ai-service.git
cd adventure-ai-service
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file with the following:
```ini
DJANGO_AUTH_URL=https://darpankattel3.pythonanywhere.com/api/auth/verify/
STACKGAN_MODEL_URL=https://huggingface.co/your-huggingface-model/stackgan
STABLE_DIFFUSION_MODEL_PATH=./stable-diffusion-v1-4
```

## Running the Server
```bash
uvicorn main:app --reload
```

API will be available at: `http://127.0.0.1:8000/docs`

## API Reference
### 1. Generate Background Image
**Endpoint:** `POST /background`
```json
{
  "prompt": "a beautiful sunset over the ocean"
}
```
**Response:**
```json
{
  "image_url": "generated_images/background_123456.png"
}
```

### 2. Generate Product Image
**Endpoint:** `POST /product-image`
```json
{
  "prompt": "a futuristic smartwatch with holographic display"
}
```
**Response:**
```json
{
  "image_url": "generated_images/product_789012.png"
}
```

## Deploying to Hugging Face Spaces
### 1. Install Hugging Face CLI
```bash
pip install huggingface_hub
huggingface-cli login
```
### 2. Push Code to Hugging Face
```bash
git init
git remote add origin https://huggingface.co/spaces/your-username/adventure-ai
git add .
git commit -m "Initial commit"
git push origin main
```
### 3. Add `space.yaml`
Create `space.yaml`:
```yaml
sdk: docker
```
### 4. Create `Dockerfile`
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```
### 5. Deploy
```bash
git add .
git commit -m "Added Docker support"
git push origin main
```

## Future Enhancements
- Implement Redis caching for faster image generation.
- Store generated images on an S3 bucket instead of local storage.
- Improve multi-threading for better performance.

## License
MIT License.

---
**Author:** Darpan Kattel
**Contact:** darpankattel1@gmail.com
**Project Repository:** [GitHub](https://github.com/darpankattel/adventure-ai-service)
