#coding=utf-8
#
# 图像像素访问.通道分离与合并
#

'''
#访问像素点，模拟带有模拟椒盐现象的图片
import cv2
import numpy as np


def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img

if __name__ == '__main__':
    img = cv2.imread("test1.jpg")
    saltImage = salt(img, 1000)
    cv2.imshow("Salt", saltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

import cv2
import numpy as np

img = cv2.imread("0601.jpg")

#分离方法1：使用OpenCV自带的split函数
b, g, r = cv2.split(img)

#分离方法2：通过访问cv2.split(img)数组来分离
#b = cv2.split(img)[0]
#g = cv2.split(img)[1]
#r = cv2.split(img)[2]

'''
分离方法3：直接操作NumPy数组来完成分离
注意：需要先要开辟一个相同大小的图片出来。这是由于numpy中数组的复制有些需要注意的地方
b = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
g = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
r = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
b[:,:] = img[:,:,0]
g[:,:] = img[:,:,1]
r[:,:] = img[:,:,2]
'''

cv2.imwrite("old/Blue.jpg", b)
cv2.imwrite("old/Red.jpg", r)
cv2.imwrite("old/Green.jpg", g)
#合并RGB(b,g,r  顺序没写对，不会合成原图)
merged = cv2.merge([b,g,r])
cv2.imshow("merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()