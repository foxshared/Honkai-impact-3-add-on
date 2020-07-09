import numpy as np
import cv2
from PIL import ImageGrab as ig
import time

import win32.win32gui as win32gui
import win32con
import win32.win32api as win32api


dc = win32gui.GetDC(0)
red = win32api.RGB(255,0,0)


def downscale_img(source, scale):
    width = int(source.shape[1]*scale/100)
    height = int(source.shape[0]*scale/100)
    dim = (width, height)
    resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
    return resized


cv2.namedWindow("test", cv2.WINDOW_NORMAL)
h = win32gui.FindWindow(None,"test")
print(h)
win32gui.SetWindowPos(h, win32con.HWND_TOPMOST, 0, 0, 0,
                      0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# handled = win32gui.WindowFromPoint((1500,212))
# handled_ = win32gui.GetDC(0)

# dc = win32gui.GetDC(0)
# red = win32api.RGB(255,0,0)

last_time = time.time()
while cv2.waitKey(1) != 27:
    time.sleep(0.5)
    # win32gui.LineTo(handled_,1400,900)
    # win32gui.SetPixel(dc,10,10,red)

    screen = ig.grab(bbox=(0, 0, 1440, 900))
    screen = downscale_img(np.array(screen), 20)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    print(time.time()-last_time)
    cv2.imshow("test", screen)
    last_time = time.time()
cv2.destroyAllWindows()
