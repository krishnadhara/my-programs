import logging
logging.basicConfig(filename="13092019.txt",level=logging.DEBUG,filemode="w",format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(levelno)d - %(message)s')
def add(x,y):
    return x/y
def sub(x,y):
    return x-y
def mul(x,y):
    return x/y
a=add(10,0)
logging.debug(a)
logging.info(a)
logging.error(a)
logging.warning(a)
logging.critical(a)

sub(10,10)
mul(10,3)