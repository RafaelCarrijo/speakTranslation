import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from fastapi.responses import JSONResponse, Response
from fastapi import status, APIRouter, UploadFile, Header
from logs.mensagem import Mensagem

#from model.schema import RequestAudio, ResponseAudio
from core.orquestrador import Orquestrador
import whisper
import ssl
import ffmpeg
import numpy as np


ssl._create_default_https_context = ssl._create_unverified_context
modelo = whisper.load_model("medium")
logger = Mensagem()
router = APIRouter()

#usado para decodificar o audio, se estiver usando mac m1 é a unica forme de se fazer
def load_audio(file_bytes: bytes, sr: int = 16_000) -> np.ndarray:
    try:
        out, _ = (
            ffmpeg.input('pipe:', threads=0, loglevel = 'quiet')
            .output("pipe:", format="s16le", acodec="pcm_s16le", ac=1, ar=sr)
            .run_async(pipe_stdin=True, pipe_stdout=True)
        ).communicate(input=file_bytes)

    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0

@router.post('/audio/upload')
async def dialogo(audio: UploadFile, linguagem: str = Header(None)):
    """
    Informações do request:
    - **Audio**: Audio que o usuario deseja traduzir"
    - **Linguagem**: Linguagem para qual o cliente deseja que o audio seja traduzida"
    """
    contents = audio.file.read()
    audio = load_audio(contents)
    orquestrador = Orquestrador(audio, linguagem, modelo)
    try:

        await orquestrador.transcrever_audio()
        audio_traduzido = await orquestrador.compila_audio()
    
        return Response(audio_traduzido)
    
    except Exception as error:
        print(error)
        logger.mensagem_error(error)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"mensagem": "Internal Server Error", "error": True})
    finally:
        del orquestrador

