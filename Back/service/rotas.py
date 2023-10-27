from fastapi.responses import JSONResponse, Response
from fastapi import APIRouter, status
from logs.mensagem import Mensagem
from model.schema import RequestAudio, ResponseAudio
from core.orquestrador import Orquestrador
import whisper

modelo = whisper.load_model("small")
logger = Mensagem()


@router.post('/audio_upload', response_model=ResponseAudio)
async def dialogo(resquest_bot: RequestAudio) -> AudioResponse:
    """
    Informações do request:
    - **Audio**: Audio que o usuario deseja traduzir"
    - **Linguagem**: Linguagem para qual o cliente deseja que o audio seja traduzida"
    """
    

    orquestrador = Orquestrador(resquest_bot, modelo)

    try:
        await orquestrador.carregar_parametro()
        response = await orquestrador.output_mensagem()

        return response
    
    except Exception as error:
        logger.error(error)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"mensagem": "Internal Server Error", "error": True})
    finally:
        del orquestrador

