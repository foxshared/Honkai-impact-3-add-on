import numpy as np
import cv2
from PIL import ImageGrab as ig
import time

def downscale_img(source, scale):
    width = int(source.shape[1]*scale/100)
    height = int(source.shape[0]*scale/100)
    dim = (width, height)
    resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)
    return resized



last_time = time.time()
while cv2.waitKey(1)!= 27:
    screen = ig.grab(bbox=(0,0,1440,900))
    screen = downscale_img(np.array(screen),20)
    screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
    print('Loop took {} seconds',format(time.time()-last_time))
    cv2.imshow("test", screen)
    last_time = time.time()
cv2.destroyAllWindows()
