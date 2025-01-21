import pyautogui
#pyautogui.mouseInfo()

#img = pyautogui.screenshot()
#55,888 206,208,214 #CED0D6
img = pyautogui.screenshot(region=(55,888, 30, 40))

img.save("icon.png")

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))