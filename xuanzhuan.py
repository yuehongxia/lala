# coding:utf-8
import numpy as np
import cv2

"""
用霍夫线变换探测出图像中的所有直线
计算出每条直线的倾斜角，求他们的平均值
根据倾斜角旋转矫正
最后根据文本尺寸裁剪图片
"""


def DegreeTrans(theta):
    """
    角度转换
    :param theta:角度
    :return: res:转换后的角度
    """
    res = theta / np.pi * 180
    return res


def rotateImage(src, degree):
    """
    逆时针旋转图像degree角度（原尺寸）
    :param src:原图
    :param degree:角度
    :return:img_rotate:旋转后的图片
    """
    # 旋转中心为图像中心
    center = [0, 0]
    imgw = src.shape[1]
    imgh = src.shape[0]
    center[0] = float(imgw / 2.0)
    center[1] = float(imgh / 2.0)
    # 计算二维旋转的仿射变换矩阵
    M = cv2.getRotationMatrix2D((center[0], center[1]), degree, 1)
    img_rotate = cv2.warpAffine(src, M, (imgw, imgh))
    return img_rotate


def CalcDegree(src):
    """
    通过霍夫变换计算角度
    :param src: 图片
    :return: degree 角度
    """
    image = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    # blurred = cv2.GaussianBlur(dstimage, (3, 3), 0)
    # midImage = cv2.Canny(dstimage, 50, 200, 3)
    # closed = cv2.erode(closed, None, iterations=4)
    # midImage = cv2.dilate(midImage, None, iterations=8)
    gradX = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0)
    gradY = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    (_, midImage) = cv2.threshold(gradient, 90, 255, cv2.THRESH_BINARY)

    cv2.imwrite('canny.jpg', midImage)
    # 通过霍夫变换检测直线
    lines = cv2.HoughLines(midImage, 1.0, np.pi / 180, 400, 0, 0)

    # 由于图像不同，阈值不好设定，因为阈值设定过高导致无法检测直线，阈值过低直线太多，速度很慢
    # 所以根据阈值由大到小设置了三个阈值，如果经过大量试验后，可以固定一个适合的阈值。
    if lines is None:
        lines = cv2.HoughLines(midImage, 1.0, np.pi / 180, 300, 0, 0)
    if lines is None:
        lines = cv2.HoughLines(midImage, 1.0, np.pi / 180, 200, 0, 0)
    if lines is None:
        print("没有检测到直线！")
        return None

    line = lines[:, 0, :]
    print(len(line))
    result = 0
    count = 0
    # 依次画出每条线段
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        if 0.8 < theta < 2.2:
            cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)
            result += theta
            count += 1
        print(theta)
    cv2.imwrite('sdf.jpg', src)

    average = result / count
    degree = DegreeTrans(average)
    return degree


def ImageRecify(imgPath, savePath):
    """
    启动方法
    :param imgPath:图片路径
    :param savePath:保存图片路径
    :return:无
    """
    src = cv2.imread(imgPath)
    degree = CalcDegree(src.copy())
    if degree is None:
        print('校正失败！')
        return
    rImg = rotateImage(src, degree)
    cv2.imwrite(savePath, rImg)
    print('angle:{}'.format(degree))


if __name__ == '__main__':
    path = '333.jpg'
    savepath = '3333.jpg'
    ImageRecify(path, savepath)

    cv2.waitKey()
    cv2.destroyAllWindows()
