import requests
import unittest
import sys
sys.path.append('D:\\seleniumscript\\InterfaceTest2\\Public')
from readxlsx import *
from logmould import recordlog
import logging

class MyTest(unittest.TestCase):
	def setUp(self):
		print('start test')
	def tearDown(self):
		print('test finish')
class InterfaceTest(MyTest):
	def test_something(self):
		datas = readxlsx(case_path)
		for data in datas:
			self.id = data[0]
			self.method = data[1]
			self.host = data[2]
			self.interface = data[3]
			self.params = eval(data[4])
			self.expected_code = data[5]
			self.isexec = data[6]
			self.api = self.host + self.interface
			if self.isexec == 0:
				# print(1)
				recordlog('case{} is not need exec'.format(self.id))
			else:
				r = requests.request(method=self.method, url=self.api, params=self.params)
				if r.status_code == self.expected_code:
					print(r.url)
					
					recordlog(r.url)
					recordlog('case{} run successfully'.format(self.id))
					pass
				else:
					recordlog(r.url)
					recordlog('case{} run failed'.format(self.id))
					pass
if __name__ == '__main__':
	unittest.main()