import os
import time
import logging

father_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
log_path = father_path + '\\testLog'
filename = time.strftime('%Y-%m-%d-%H') + '.log'
fullfile = log_path + '\\' + filename
def recordlog(infomation):
	root = logging.getLogger('interface')
	formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	root.setLevel(level=logging.INFO)
	handler = logging.FileHandler(fullfile)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(formatter)

	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	console.setFormatter(formatter)

	root.addHandler(handler)
	root.addHandler(console)
	root.info(infomation)
	root.removeHandler(handler)
	root.removeHandler(console)


# def add1(x, y):
# 	return x + y
# if __name__ == '__main__':
# 	recordlog('world')
# 	recordlog('world')
# 	recordlog('world')
# 	recordlog('world')
# 	recordlog('world')