
import xlrd
import os

class DoExcel:

    def __init__(self, filename):

        self.xl = xlrd.open_workbook(filename)
        self.sheet = self.xl.sheet_by_index(0)

    def getExcelValue(self, rowNum, colNum):

        excelValue = self.sheet.cell(rowNum, colNum).value
        return excelValue


if __name__ == "__main__":

    file = os.path.dirname(os.path.abspath('./..')) + '/Data/TestData.xls'
    print(file)

    excel = DoExcel(file)
    value = excel.getExcelValue(1, 2)
    print(value)