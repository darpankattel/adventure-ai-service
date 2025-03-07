FROM python:3.9
WORKDIR /app
COPY . /app
RUN mkdir -p /app/cache && chmod -R 777 /app/cache
RUN mkdir -p /app/models/generated_images && chmod -R 777 /app/models/generated_images
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]