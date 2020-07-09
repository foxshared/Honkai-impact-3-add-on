import fps_counter_lib
import time
from PIL import ImageGrab as ig
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import win32.win32gui as win32gui
from win32.lib import win32con
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
        # cv2.namedWindow("target", cv2.WINDOW_NORMAL)
        # cv2.namedWindow("target2", cv2.WINDOW_NORMAL)

        win32gui.SetWindowPos(win32gui.FindWindow(None, "game_screen"), win32con.HWND_TOPMOST, 0,
                              0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # win32gui.SetWindowPos(win32gui.FindWindow(None, "target"), win32con.HWND_TOPMOST, 0,
        #                       0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # win32gui.SetWindowPos(win32gui.FindWindow(None, "target2"), win32con.HWND_TOPMOST, 0,
        #                       0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        self.run_()

    def run_(self):
        last_time = time.time()

        while cv2.waitKey(1) != 27:
            # time.sleep(0.1)
            a = []
            test1 = cv2.cvtColor(cv2.imread(
                "img.jpg"), cv2.COLOR_BGR2GRAY)
            intial_shape = test1.shape

            b = win32gui.FindWindow(None, "Honkai Impact 3")
            # b = win32gui.FindWindow(None, "File Explorer")

            game_position = win32gui.GetWindowRect(b)
            edit_position = (game_position[0],game_position[1]+30,game_position[2],game_position[3])
            print(edit_position)
            game_screen = np.array(ig.grab(edit_position))
            game_screen = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)

            screen_size = game_screen.shape
            w, h = screen_size[1], screen_size[0]
            # new_list = [w, h]
            # a.append(new_list)

            test2 = self.set_size(test1, w, h)
            size_up = test2.shape

            dif_x1, dif_y1, dif_x2, dif_y2 = self.get_new_size(
                intial_shape, size_up, 22, 32, 78, 87)

            button1 = test2[dif_y1:dif_y2, dif_x1:dif_x2]
            button2 = game_screen[dif_y1:dif_y2, dif_x1:dif_x2]
            # print(dif_w,dif_h)

            p1 = (abs(dif_x1), abs(dif_y1))
            p2 = (abs(dif_x2), abs(dif_y2))
            # rec = cv2.rectangle(game_screen,p1,p2, (0, 255, 255), 2)

            if button1.shape == button2.shape:
                same = ssim(button1, button2)
                # print(same)

            # font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            # fontsize, color, thickness = 2, (255, 0, 0), 2
            # screen = cv2.putText(game_screen, str(
            #     a), (10, 30), font, fontsize, color, thickness, cv2.LINE_AA)
            image = np.concatenate((button2,button1),axis=1)
            cv2.imshow("game_screen", game_screen)
            

            # cv2.imshow("rec draw", rec)

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

    def get_new_size(self, intial_shape, end_shape, x1=0, y1=0, x2=0, y2=0):
        intial_w, intial_h = intial_shape[1], intial_shape[0]
        end_w, end_h = end_shape[1], end_shape[0]
        per_w = round(((end_w/intial_w)*100), 2)
        per_h = round(((end_h/intial_h)*100), 2)
        # print(per_w,per_h)

        dif_x1 = int(((per_w/100)*x1))  # x1
        dif_y1 = int(((per_h/100)*y1))  # y1

        dif_x2 = int(((per_w/100)*x2))  # x2
        dif_y2 = int(((per_h/100)*y2))  # y2
        return dif_x1, dif_y1, dif_x2, dif_y2

    def capture(self, tar):
        print("capture")
        cv2.imwrite("img.jpg", tar)


fps = fps_counter_lib.FPS_counter()
application()
