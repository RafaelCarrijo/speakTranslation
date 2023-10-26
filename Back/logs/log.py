import sys
import logging
import colorlog


class LoggerBot():
    def __init__(self, disable :bool = False) -> None:
        """Classe de log personalizada 

        Args:
            disable (bool, optional): _description_. Defaults to False.
        """
        self.logger = logging.getLogger('')
        self.logger.setLevel(logging.INFO)

        fh = logging.FileHandler('log_info.log')
        sh = logging.StreamHandler(sys.stdout)
        
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', 
                                        datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)

        sh.setFormatter(colorlog.ColoredFormatter('%(log_color)s [%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
                                        datefmt='%a, %d %b %Y %H:%M:%S'))


        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
