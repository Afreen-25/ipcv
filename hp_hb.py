# -*- coding: utf-8 -*-
"""hp_hb.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mr7IA-m9PK42jZIn0Epf5R6C2fwboPQC
"""

from google.colab.patches import cv2_imshow
import cv2
import numpy as np

# Read the image
img = cv2.imread('/content/beautiful-nature-scenery-free-photo (1).jpg', 0)
h, w = img.shape

# Display the original image
cv2_imshow(img)

# High pass filter
mask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
hp_img = cv2.filter2D(img, -1, mask)

# Display the image after high pass filtering
cv2_imshow(hp_img)

# High boost filter
a = 1.1
mask = np.array([[-1, -1, -1], [-1, 8 + a, -1], [-1, -1, -1]])
hb_img = cv2.filter2D(img, -1, mask)

# Display the image after high boost filtering
cv2_imshow(hb_img)

# Ideal high pass
F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
H = np.zeros((h, w), dtype=np.float32)
D0 = 50

for i in range(h):
    for j in range(w):
        D = np.sqrt((i - h / 2) ** 2 + (j - w / 2) ** 2)
        if D < D0:
            H[i][j] = 1
        else:
            H[i][j] = 0

Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

# Display the ideal high pass filter
cv2_imshow(H)

# Display the resulting image after applying the ideal high pass filter
cv2_imshow(g)

# Ideal low pass
H = 1 - H
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

# Display the resulting image after applying the ideal low pass filter
cv2_imshow(g)

# Read the image
img = cv2.imread('/content/beautiful-nature-scenery-free-photo (1).jpg', 0)
h, w = img.shape

# Display the original image
cv2_imshow(img)
cv2.waitKey(0)

# High pass filter
mask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
hp_img = cv2.filter2D(img, -1, mask)

# Display the image after high pass filtering
cv2_imshow(hp_img)
cv2.waitKey(0)

# High boost filter
a = 1.1
mask = np.array([[-1, -1, -1], [-1, 8 + a, -1], [-1, -1, -1]])
hb_img = cv2.filter2D(img, -1, mask)

# Display the image after high boost filtering
cv2_imshow(hb_img)
cv2.waitKey(0)

# Ideal high pass
F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
H = np.zeros((h, w), dtype=np.float32)
D0 = 50

for i in range(h):
    for j in range(w):
        D = np.sqrt((i - h / 2) ** 2 + (j - w / 2) ** 2)
        if D < D0:
            H[i][j] = 1
        else:
            H[i][j] = 0

Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

# Display the ideal high pass filter
cv2_imshow(H)
cv2.waitKey(0)

# Display the resulting image after applying the ideal high pass filter
cv2_imshow(g)

# Ideal low pass
H = 1 - H
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

# Display the resulting image after applying the ideal low pass filter
cv2_imshow(g)
