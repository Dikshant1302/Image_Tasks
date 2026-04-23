from fastapi import FastAPI, UploadFile, File
import base64
from rembg import remove
import asyncio
import ollama

app = FastAPI()

# 🔥 Async wrapper for CPU-heavy tasks
async def remove_bg_async(image_bytes):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, remove, image_bytes)

# 🔥 Async wrapper for Ollama
async def get_caption(image_bytes):
    loop = asyncio.get_event_loop()

    def call_ollama():
        response = ollama.chat(
            model="moondream",
            messages=[{
                "role": "user",
                "content": "Describe this image in one sentence.",
                "images": [image_bytes]
            }]
        )
        return response['message']['content']

    return await loop.run_in_executor(None, call_ollama)


@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        # Run both tasks concurrently 🔥
        caption_task = asyncio.create_task(get_caption(image_bytes))
        bg_task = asyncio.create_task(remove_bg_async(image_bytes))

        description = await caption_task
        output_bytes = await bg_task

        # Convert image to base64
        encoded_image = base64.b64encode(output_bytes).decode("utf-8")

        return {
            "description": description,
            "image": encoded_image
        }

    except Exception as e:
        return {"error": str(e)}