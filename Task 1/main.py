from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

app = FastAPI()

def process_image(image_bytes):
    return remove(image_bytes)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        input_bytes = await file.read()
        output_bytes = process_image(input_bytes)

        return StreamingResponse(
            io.BytesIO(output_bytes),
            media_type="image/png"
        )

    except Exception as e:
        return {"error": str(e)}