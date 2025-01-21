import pyautogui

img = pyautogui.screenshot()
img.save("screenshot.png")

#pyautogui.mouseInfo()

#744,377 29,30,33 #1D1E21
pixel = pyautogui.pixel(744,377)
print(pixel)

print(pyautogui.pixelMatchesColor(744,377,(29,30,33)))
print(pyautogui.pixelMatchesColor(744,377,(29,30,pixel)))

