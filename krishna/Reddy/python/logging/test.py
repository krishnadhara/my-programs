import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.WARNING)

file_handler =logging.FileHandler('test2.log')

format= '%(asctime)s - %(funcName)s - %(name)s - %(filename)s - %(levelname)s - %(levelno)d - %(message)s'

formatter =logging.Formatter(format)
file_handler.setFormatter(formatter)
logger.addHandler((file_handler))
logger.warning("this is wornng from test.py")
