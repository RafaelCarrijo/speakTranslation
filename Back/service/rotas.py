from fastapi.responses import JSONResponse, Response
from fastapi import APIRouter, status
from typing import Union, Optional, Dict
from logs.mensagem import Mensagem
from model.schema import RequestAudio, ResponseAudio
from core.orquestrador import Orquestrador

logger = Mensagem()


@router.post('/audio_upload', response_model=ResponseAudio)
async def dialogo(resquest_bot: RequestAudio) -> AudioResponse:
    """
    Informações do request:
    - **Audio**: Audio que o usuario deseja traduzir"
    - **Linguagem**: Linguagem para qual o cliente deseja que o audio seja traduzida"
    """
    

    orquestrador = Orquestrador(resquest_bot)

    try:
        orquestrador.carregar_parametro
        await orquestrador.intent_entidade
        await orquestrador.processar_negocio()
        await orquestrador.recuperar_acao()
        response = await orquestrador.output_mensagem()

        return response
    
    except Exception as error:
        logger.error(error)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"mensagem": "Internal Server Error", "error": True})
    finally:
        del orquestrador

