import cv2
import numpy as np
from win32 import win32gui
from pythonwin import win32ui
from win32.lib import win32con
from win32 import win32api

from grab_screen import grab_screen

import time

# img = grab_screen()
# cv2.imshow('frame',img)

def downscale_img(source, scale):
    width = int(source.shape[1]*scale/100)
    height = int(source.shape[0]*scale/100)
    dim = (width, height)
    resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
    return resized

a = time.time()
while cv2.waitKey(1)!=27:
    # frame = grab_screen((0,0,100,100))
    frame = grab_screen()
    frame = downscale_img(frame,20)
    cv2.imshow('frame',frame)
    print(time.time()-a)
    a = time.time()

cv2.destroyAllWindows()