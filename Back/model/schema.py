from pydantic import BaseModel, Field


class RequestAudio(BaseModel):
    audio: bytes = Field(None, title="Audio de usuario recebido em qualquer lingua") 
    linguagem: str = Field("Portugues", title="linguagem em que a resposta deve ser devolvida")


class ResponseAudio(BaseModel):
    audio: bytes = Field(None, title="Audio do usuario depois da tradução") 
    linguagem_original: str = Field("Linguagem original do texto: portugues", title="linguagem original") 
    error: bool = Field(False, title="variavel booleana com indicativo de erro") 
 
     

    