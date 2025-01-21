from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

image_path = "fubao.png"
img = Image(image_path)

ws.add_image(img, "C3")

wb.save("sample_image.xlsx")

#pip install Pillow
