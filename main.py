from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

@app.get(
    "/downloadfile/{filename}",
    response_class=FileResponse
)
async def download_file(filename:str):
    if not Path(f"uploads/{filename}").exists():
        raise HTTPException(
            status_code=404,
            detail=f"file {filename} not found"
        )
    return FileResponse(
        path=f"uploads/{filename}", filename=filename
    )