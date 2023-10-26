
from typing import Dict, Text

from logs.mensagem import Mensagem

logger = Mensagem()


class Orquestrador():

    audio: Text
    linguagem: Text


    
    def __init__(self, dados: Dict) -> None:
        """Classe que orquestrar as funcionalidades do tradutor
        Args:
            Audio (Bytes): Audio na linguagem original
            linguagem (Text): linguagem destino
        """
        self.audio = dados.audio
        self.linguagem = dados.linguagem


    @property
    def carregar_parametro(self) -> None:
        """Carregar parametros de entrada 
        """       
        try:
            pass
        except Exception as ex:
            logger.mensagem_error(f"Erro: {ex}")
            raise ex
        

        


    async def output_mensagem(self) -> Dict:
        return {
            
        }

