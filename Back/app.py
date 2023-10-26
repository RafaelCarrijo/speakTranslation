import os
from fastapi import (Depends,
                    FastAPI,
                    Header,
                    HTTPException,
                    status)

from service import rotas


async def verificar_token(token: str = Header(...)):
    """Verificar token no header 
    Args:
        token (str, optional): _description_. Defaults to Header(...).
    Raises:
        HTTPException: Se o token não estiver correto retorna erro
    """
    if token != os.environ['SECRET_KEY']:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="SECRET_KEY header invalid")


app = FastAPI(title="Tradução de áudios",
              description="Recebe um audio em qualquer idioma, detecta a linguagem original, traduz e devolve o audio traduzido",
              version="0.01.beta")
              #dependencies=[Depends(verificar_token)])

app.include_router(rotas.router, tags=['Tradutor'])
