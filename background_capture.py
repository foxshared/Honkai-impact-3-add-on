from pythonwin import win32ui
import win32.win32gui as win32gui
from win32.lib import win32con
import cv2
import numpy as np
import time
from PIL import ImageGrab as grab

# Make current file path as working environment
import os
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)

def background_screenshot(hwnd, width, height):
    width,height = width,height
    print(width,height)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (0, 0), win32con.SRCCOPY)

    a = dataBitMap.GetBitmapBits(False)
    img_ = np.array(a).astype(dtype="uint8")
    img_.shape = (height, width, 4)

    cv2.imshow("pre",img_)
    # dcObj.DeleteDC()
    # cDC.DeleteDC()
    # win32gui.ReleaseDC(hwnd, wDC)
    # win32gui.DeleteObject(dataBitMap.GetHandle())


b = win32gui.FindWindow(None, "Rufus")

win32gui.ShowWindow(b, 10)
win32gui.SetForegroundWindow(b)
y = win32gui.GetWindowRect(b)
# print(y)
info = np.array(grab.grab(y))

w, h = info.shape[1], info.shape[0]

time.sleep(1)
win32gui.CloseWindow(b)

y = win32gui.GetWindowRect(b)
try:
    while cv2.waitKey(1) != 27:
        background_screenshot(b, w, h)
except Exception as e:
    print(e)
    pass
cv2.destroyAllWindows()
