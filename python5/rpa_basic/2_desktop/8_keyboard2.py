import pyautogui
# pip install pyperclip

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

import pyperclip
#pyperclip.copy("코딩연습")
#pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("코딩연습")