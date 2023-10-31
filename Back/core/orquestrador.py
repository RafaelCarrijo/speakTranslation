
from typing import Text
from logs.mensagem import Mensagem
from gtts import gTTS
from io import BytesIO
import numpy as np
import whisper

logger = Mensagem()

class Orquestrador():

    audio: Text
    linguagem: Text
    
    def __init__(self, audio :np.array, linguagem: str, modelo: object) -> None:
        """Classe que orquestrar as funcionalidades do tradutor
        Args:
            Audio (Bytes): Audio na linguagem original
            Linguagem (Text): linguagem destino
            Modelo (Classe): modelo carregado fora do request para aumentar performance
        """
        self.audio = audio
        self.linguagem = linguagem
        self.modelo = modelo
        self.text = ""
        self.stream = BytesIO()
        


    async def detectar_idioma(self) -> None:
        """Detecta o idioma original do audio
        """       
        try:

            #cortando o audio para deixar com apenas 30 segundos
            audio = whisper.pad_or_trim(self.audio)
            #trabalhando o audio de forma performatica para cada tipo de processador que estiver sendo utilizado
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

            #detecta a linguagem com a maior probabilidade de ter sido utilizada no audio original
            #criando um dicionario para facilitar o retorno da linguagem com maior probabilidade
            _, probs = self.model.detect_language(mel)

            #retorna apenas a linguagem detectada
            print(max(probs, key=probs.get))
            return max(probs, key=probs.get)

        except Exception as ex:
            logger.mensagem_error(f"Erro: {ex}")
                


    async def transcrever_audio(self) -> None:
        """Transcreve o audio na linguagem solicitada
        """  
            
        try:
            #utilizado o metodo tarnscribe direto para a linguagem destino.
            #com ele podemos processar audios maiores que 30 segundos
            self.text = self.modelo.transcribe(self.audio, language=self.linguagem)['text']
            
        except Exception as ex:
            logger.mensagem_error(f"Erro: {ex}")
            

    async def compila_audio(self) -> str:

        audio = gTTS(text=self.text, lang=self.linguagem, slow=False)
        audio.write_to_fp(self.stream)

        return self.stream.getvalue()
        

