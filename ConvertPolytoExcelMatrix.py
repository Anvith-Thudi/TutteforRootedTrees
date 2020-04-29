import xlsxwriter

import xlrd

def convert_excel(polynomial):
	workbook = xlsxwriter.Workbook('Polys12.xlsx')

	for data in polynomial:
    		worksheet=workbook.add_worksheet()
    		for term in data:
        		worksheet.write(term[2],term[1],term[0])

	workbook.close()