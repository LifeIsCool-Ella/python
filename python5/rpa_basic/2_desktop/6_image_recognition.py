import pyautogui
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

import time
#file_menu = pyautogui.locateOnScreen("file_menu.png")

#print(file_menu)
#pyautogui.click(file_menu)


#trash_icon = pyautogui.locateOnScreen("trash_icon.png")
#pyautogui.moveTo(trash_icon)

#screen = pyautogui.locateOnScreen("screenshot.png")
#print(screen)

#for i in pyautogui.locateAllOnScreen("checkbox.png"):
#    print(i)
#    pyautogui.click(i, duration=0.25)

#checkbox = pyautogui.locateOnScreen("checkbox.png")
#pyautogui.click(checkbox)


#trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
#pyautogui.moveTo(trash_icon)


#trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881-1488,760-623))
#pyautogui.moveTo(trash_icon)

#run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.7)
#pyautogui.moveTo(run_btn)

#pip install opencv-python
#run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.7)
#pyautogui.moveTo(run_btn)

#file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#if file_menu_notepad:
#    pyautogui.click(file_menu_notepad)
#else:
#    print("발견 실패")

#while file_menu_notepad is None:

#    print("발견 실패")

#pyautogui.click(file_menu_notepad)

import time
import sys

#timeout = 10
#start = time.time()
#file_menu_notepad = None
#while file_menu_notepad is None:
#    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#    end = time.time()
#    if end - start > timeout :
#        print("시간 종료")
#        sys.exit()
#pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[timeout {timeout}s] Target not found ({img_file}). Terminate Program ")
        sys.exit()

my_click("file_menu_notepad.png", 10)