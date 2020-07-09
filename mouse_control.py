import pyautogui

import pynput

try:
    while True:
        x, y = pyautogui.position()
        print(x,y,pyautogui.size())
        # pyautogui.keyDown("n")
        
except KeyboardInterrupt:
    print('\n')