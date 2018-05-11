import xlrd
import os

father_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
case_path = father_path + '\\testCase' + '\\casedata.xlsx'

def readxlsx(filepath):
	workbook = xlrd.open_workbook(case_path)
	booksheet = workbook.sheet_by_name('interfacecase')
	p = list()
	for row in range(1, booksheet.nrows):
		row_data = []
		for col in range(booksheet.ncols):
			cel = booksheet.cell(row, col)
			val = cel.value
			if type(val) == float:
				val = int(val)
			else:
				val = str(val)
			row_data.append(val)
		p.append(row_data)
	return p

if __name__ == '__main__':	
	datas = readxlsx(case_path)
	# print(datas)
	for data in datas:
		print(data)
	# for i in range(len(data)):
	# 	for j in range(len(data[i])):
	# 		print(data[i][j])

