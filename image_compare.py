from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np

# Make current file path as working environment
import os
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)
import time
a = time.time()

test1 = cv2.cvtColor(cv2.imread("test_1.png"),cv2.COLOR_BGR2GRAY)
test2 = cv2.cvtColor(cv2.imread("test_2.png"),cv2.COLOR_BGR2GRAY)


s = ssim(test1,test2)
b = time.time() - a
print(s,b)

