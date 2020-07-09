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

        self.b = win32gui.FindWindow(None,"File Explorer")
        
        cv2.namedWindow("game_screen", cv2.WINDOW_NORMAL)
        s = win32gui.FindWindow(None,"game_screen")
        win32gui.SetWindowPos(s, win32con.HWND_TOPMOST, 0,
                              0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        self.run()

    def run(self):
        last_time = time.time()

        test1 = cv2.cvtColor(cv2.imread("test1_game.png"), cv2.COLOR_BGR2GRAY)
        test1 = test1[0:900,int(1440/2):1440]
        test1 = self.downscale_img(np.array(test1), 80)
        

        while cv2.waitKey(1) != 27:
            # time.sleep(0.5)

            game_position = win32gui.GetWindowRect(self.b)
            try:
                game_screen = ig.grab(game_position)
                game_screen = self.downscale_img(np.array(game_screen), 80)
                cv2.imshow("game_screen",game_screen)
            except:
                print("None")
                pass

            screen = ig.grab(bbox=(0, 0, 1440, 900))
            screen = np.array(screen)
            screen = screen[0:900,int(1440/2):1440]
            screen = self.downscale_img(screen, 80)
            
            screen1 = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            print(screen.shape,game_screen.shape)
            s = ssim(test1, screen1)
            s = round(s,2)
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            fontsize ,color,thickness=1,(255,0,0),2
            screen = cv2.putText(screen,str(s),(10,30),font,fontsize,color,thickness,cv2.LINE_AA)
            print((time.time()-last_time),game_position)
            cv2.imshow("test", screen)
            # cv2.imshow("image",test1)
            last_time = time.time()
        cv2.destroyAllWindows()

    def downscale_img(self, source, scale):
        width = int(source.shape[1]*scale/100)
        height = int(source.shape[0]*scale/100)
        dim = (width, height)
        resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
        return resized


application()
