# -*- coding: utf-8 -*-
"""thresholding_greylevel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15QSUYATWvqjt_gn_q7hu6GfXF5d1ZytE
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img1 = cv2.imread('/content/beautiful-nature-scenery-free-photo (1).jpg')

grey_img1 = cv2.imread('/content/beautiful-nature-scenery-free-photo (1).jpg', 0)
h, w = grey_img1.shape

# Digital Negative
neg_img = 255 - grey_img1

# Thresholding
t = 50
threshold_img = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        if grey_img1[i][j] > t:
            threshold_img[i][j] = 255
        else:
            threshold_img[i][j] = 0

# Grey level Slicing with BG
a = 150
b = 175
wbg_img = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        r = grey_img1[i][j]
        if a <= r <= b:
            wbg_img[i][j] = 255
        else:
            wbg_img[i][j] = r

# Grey level Slicing without BG
wobg_img = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        if a <= grey_img1[i][j] <= b:
            wobg_img[i][j] = 255
        else:
            wobg_img[i][j] = 0

cv2_imshow(neg_img)
cv2_imshow(threshold_img)
cv2_imshow(wbg_img)
cv2_imshow(wobg_img)
cv2.waitKey()

