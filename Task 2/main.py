from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove, new_session
import io

app = FastAPI()

session = new_session()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        input_bytes = await file.read()

        output_bytes = remove(input_bytes, session=session)

        return StreamingResponse(
            io.BytesIO(output_bytes),
            media_type="image/png",
            headers={"Content-Disposition": "attachment; filename=output.png"}
        )

    except Exception as e:
        return {"error": str(e)}