#coding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread(r'15.jpg')
kernel = np.ones((10, 10), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imwrite('fushi/15_.jpg',erosion)
plt.subplot(121), plt.imshow(image), plt.title('Origin')
plt.subplot(122), plt.imshow(erosion), plt.title('Erode')
plt.show()
