
from typing import Dict, Text
from logs.mensagem import Mensagem
import whisper

logger = Mensagem()

class Orquestrador():

    audio: Text
    linguagem: Text


    
    def __init__(self, dados: Dict, modelo) -> None:
        """Classe que orquestrar as funcionalidades do tradutor
        Args:
            Audio (Bytes): Audio na linguagem original
            linguagem (Text): linguagem destino
        """
        self.audio = dados.audio
        self.linguagem = dados.linguagem
        self.modelo = modelo


    def transcrever_audio(self) -> None:
        """Transcreve o audio na linguagem solicitada
        """  
            
        try:
            self.audio = whisper.load_audio(self.audio) 
            
        except Exception as ex:
            logger.mensagem_error(f"Erro: {ex}")
            raise ex
        

    def detectar_idioma(self) -> None:
        """Detecta o idioma original do audio
        """       
        try:
            pass
        except Exception as ex:
            logger.mensagem_error(f"Erro: {ex}")
            raise ex        


    async def output_mensagem(self) -> Dict:
        return {
            
        }

