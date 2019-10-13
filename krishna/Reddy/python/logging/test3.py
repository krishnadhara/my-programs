import logging
logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(funcName)s - %(name)s - %(filename)s - %(levelname)s - %(levelno)d - %(message)s',
                    filename='test.log')
def test():
    logging.debug("dbug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")
test()