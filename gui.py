import pyautogui
import time
import random

screenWidth, screenHeight = pyautogui.size()


while True:
    # x = random.randint(0, screenWidth)
    # y = random.randint(0, screenHeight)
    # pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(5)