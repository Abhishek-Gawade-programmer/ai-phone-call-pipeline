from datetime import datetime
import io
from fastapi import FastAPI, HTTPException, UploadFile, Depends
from fastapi.responses import StreamingResponse
import logging
import os
from config import get_stt_provider, get_llm_provider, get_tts_provider
from services.call_pipeline import CallPipelineService

from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


PIPELINE = CallPipelineService(
    get_stt_provider(os.getenv("DEEPGRAM_API_KEY")),
    get_llm_provider(os.getenv("OPENAI_API_KEY")),
    get_tts_provider(os.getenv("ELEVENLABS_API_KEY")),
)


@app.post("/call")
async def process_call(file: UploadFile):
    """
    Endpoint to process a call by handling the uploaded audio file.

    Args:
        file (UploadFile): The uploaded audio file.
        call_pipeline (CallPipelineService): The call pipeline service to handle the call.

    Returns:
        dict: A dictionary containing the response audio.
    """

    audio_data = await file.read()

    response_audio = await PIPELINE.handle_call(audio_data)
    return StreamingResponse(io.BytesIO(response_audio), media_type="audio/wav")


@app.get("/health")
async def health_check():
    """Check health of all providers"""
    try:

        status = await PIPELINE.health_check()
        return {
            "status": "healthy" if all(status.values()) else "degraded",
            "providers": status,
            "timestamp": datetime.utcnow().isoformat(),
        }
    except Exception as e:
        logger.error(f"Health check error: {str(e)}")
        raise HTTPException(status_code=500, detail="Health check failed")
