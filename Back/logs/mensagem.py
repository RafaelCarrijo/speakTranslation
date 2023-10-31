from typing import Text
from logs.log import LoggerBot

class Mensagem(LoggerBot):
    """Classe reponsavel de mensagem
    Args:
        object (_type_): _description_
    """
    def __init__(self):

        super().__init__()

    def mensagem_default(self, msg: Text) -> None:
        self.logger.info(f"{msg}")
        return {'mensagem': msg, 'error': False}    

    def mensagem_error(self, msg: Text) -> None:
        self.logger.debug(f"{msg}")
        return {'mensagem': msg, 'error': True}    

    def mensagem_exception(self, msg: Text) -> None:
        self.logger.error(f"{msg}")
        return {'mensagem': msg, 'error': True}    

