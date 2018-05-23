# coding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'13.jpg')
kernel = np.ones((5, 5), np.uint8)
open_img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imwrite('13___.jpg', image)
plt.imshow(image)
plt.imshow(open_img)
plt.show()