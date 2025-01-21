# pip install openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "NewSheet"
wb.save("sample.xlsx")
wb.close()