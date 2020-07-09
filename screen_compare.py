import time
from PIL import ImageGrab as ig
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import win32.win32gui as win32gui
import win32con

# Make current file path as working environment
import os
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)


def downscale_img(source, scale):
    width = int(source.shape[1]*scale/100)
    height = int(source.shape[0]*scale/100)
    dim = (width, height)
    resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
    return resized


last_time = time.time()
test1 = cv2.cvtColor(cv2.imread("test_1.png"), cv2.COLOR_BGR2GRAY)
test1 = downscale_img(np.array(test1), 20)

while cv2.waitKey(1) != 27:

    screen = ig.grab(bbox=(0, 0, 1440, 900))
    screen = downscale_img(np.array(screen), 20)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    s = ssim(test1, screen)
    print('Loop took {} seconds', format(time.time()-last_time), s)
    cv2.imshow("test", screen)
    last_time = time.time()
cv2.destroyAllWindows()
