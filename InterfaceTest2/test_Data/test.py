# import sys
# sys.path.append('D:\\seleniumscript\\InterfaceTest2\\Public')
# from logmould import recordlog

# recordlog('hello_world')
import logging
# print(dir(logging.FileHandler('log.log')))
logger = logging.getLogger()
sc = logging.FileHandler('log.log')
logger.addHandler(sc)
logger.warn('debug')
logger.warn('debug')
logger.warn('debug')
logger.warn('debug')