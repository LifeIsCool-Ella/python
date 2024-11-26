# pip install Pillow

import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1, 11):
    img = ImageGrab.grab()
    #img.save("/python3/gui_project/images/image{}.png".format(i)) 
    img.save("image{}.png".format(i)) 
    time.sleep(2)