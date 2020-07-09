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


class application():
    def __init__(self):
        cv2.namedWindow("test", cv2.WINDOW_NORMAL)
        h = win32gui.FindWindow(None, "test")
        win32gui.SetWindowPos(h, win32con.HWND_TOPMOST, 0,
                              0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        self.run()

    def run(self):
        last_time = time.time()
        test1 = cv2.cvtColor(cv2.imread("test_1.png"), cv2.COLOR_BGR2GRAY)
        test1 = self.downscale_img(np.array(test1), 20)

        while cv2.waitKey(1) != 27:
            time.sleep(0.5)
            screen = ig.grab(bbox=(0, 0, 1440, 900))
            screen = self.downscale_img(np.array(screen), 20)
            screen1 = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            s = ssim(test1, screen1)
            s = round(s,2)
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            fontsize ,color,thickness=1,(255,0,0),2
            screen = cv2.putText(screen,str(s),(10,30),font,fontsize,color,thickness,cv2.LINE_AA)
            print('Loop took {} seconds', format(time.time()-last_time), s)
            cv2.imshow("test", screen)
            last_time = time.time()
        cv2.destroyAllWindows()

    def downscale_img(self, source, scale):
        width = int(source.shape[1]*scale/100)
        height = int(source.shape[0]*scale/100)
        dim = (width, height)
        resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
        return resized


application()
