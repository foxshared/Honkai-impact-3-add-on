import fps_counter_lib
import time
from PIL import ImageGrab as ig
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import win32.win32gui as win32gui
import win32con
import threading

# Make current file path as working environment
import os
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)


cv2.setUseOptimized(True)
print(cv2.useOptimized())


class application(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        fps.start_fps()
        cv2.namedWindow("game_screen", cv2.WINDOW_NORMAL)
        cv2.namedWindow("target", cv2.WINDOW_NORMAL)
        s = win32gui.FindWindow(None, "game_screen")
        win32gui.SetWindowPos(s, win32con.HWND_TOPMOST, 0,
                              0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        e = win32gui.FindWindow(None, "target")
        win32gui.SetWindowPos(e, win32con.HWND_TOPMOST, 0,
                              0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        self.run_()

    def run_(self):
        last_time = time.time()

        # test1 = test1[0:900, int(1440/2):1440]
        # test1 = self.downscale_img(np.array(test1), 50)

        while cv2.waitKey(1) != 27:
            # time.sleep(0.3)
            a = []
            test1 = cv2.cvtColor(cv2.imread(
                "test1_game.png"), cv2.COLOR_BGR2GRAY)

            try:
                b = win32gui.FindWindow(None, "Honkai Impact 3")
                # b = win32gui.FindWindow(None, "This PC")
                game_position = win32gui.GetWindowRect(b)

                game_screen = np.array(ig.grab(game_position))
                game_screen = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)
                screen_size = game_screen.shape
                # game_screen = self.downscale_img(game_screen, 80)

                new_list = [screen_size[1], screen_size[0]]
                a.append(new_list)

                test1 = self.set_size(test1, screen_size[1], screen_size[0])

                # print(test1.shape,game_screen.shape)
                if test1.shape == game_screen.shape:
                    same = ssim(test1, game_screen)
                    print(same)

                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                fontsize, color, thickness = 2, (255, 0, 0), 2
                screen = cv2.putText(game_screen, str(
                    a), (10, 30), font, fontsize, color, thickness, cv2.LINE_AA)

                cv2.imshow("game_screen", game_screen)
                cv2.imshow("target", test1)

            except:
                pass
            # print(fps.update_fps())
            # print((time.time()-last_time))
            # last_time = time.time()
        cv2.destroyAllWindows()

    def downscale_img(self, source, scale):
        width = int(source.shape[1]*scale/100)
        height = int(source.shape[0]*scale/100)
        dim = (width, height)
        resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
        return resized

    def set_size(self, src, w, h):
        return cv2.resize(src, (w, h), interpolation=cv2.INTER_AREA)


fps = fps_counter_lib.FPS_counter()
application()
