# -*- coding: utf-8 -*-
"""salt-pepper-avg-median.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18e9Kzw3qnKFJrCZRgF_KCbSEl_GRhWuG
"""

import cv2
import numpy as np
import math
import random
from google.colab.patches import cv2_imshow
img = cv2.imread('/content/beautiful-nature-scenery-free-photo (1).jpg', 0)
h, w = img.shape

# Averaging Filter

noise = np.random.normal(0, 50, size=img.shape)
noisy_img = img + noise

cv2_imshow(noisy_img)
cv2.waitKey(5000)  # Display the image for 5 seconds

mask = np.ones((3, 3), dtype=int) / 9

avg_filtered_img = cv2.filter2D(img, -1, mask)

print(mask)
print(np.allclose(img, avg_filtered_img))  # Check if the filtering operation is correct

cv2_imshow(avg_filtered_img)
cv2.waitKey(5000)  # Display the image for 5 seconds

# Median Filter

snp = img.copy()

for i in range(35000):
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    snp[y][x] = 255

for i in range(35000):
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    snp[y][x] = 0

cv2_imshow(snp)
cv2.waitKey(5000)  # Display the image for 5 seconds

snp_removed_img = cv2.medianBlur(snp, 3)

cv2_imshow(snp_removed_img)
cv2.waitKey(5000)  # Display the image for 5 seconds

