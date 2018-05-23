import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r'15.jpg')
kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite('pengzhang/15__.jpg',dilate)
plt.subplot(121), plt.imshow(image), plt.title('Origin')
plt.subplot(122), plt.imshow(dilate), plt.title('Dilate')
plt.show()

