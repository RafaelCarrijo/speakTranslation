from pydantic import BaseModel, Field
from fastapi import UploadFile


class RequestAudio(BaseModel):
    audioFile: UploadFile
    linguagem: str = Field("Portugues", title="Linguagem em que a resposta deve ser devolvida")


class ResponseAudio(BaseModel):
    audio: bytes = Field("", title="Audio do usuario depois da tradução") 
    error: bool = Field(False, title="Variavel booleana com indicativo de erro") 
 
     

    