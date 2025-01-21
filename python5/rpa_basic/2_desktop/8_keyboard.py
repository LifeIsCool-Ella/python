import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

pyautogui.write("12345", interval=0.25)
pyautogui.write("CodingTest", interval=0.25)

pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)

pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")


pyautogui.hotkey("ctrl","alt","shift","a")

pyautogui.hotkey("ctrl", "a")
