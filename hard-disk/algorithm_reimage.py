# 图像裁剪函数

import math


def reimage(image, circle):
    for y in range(800):
        for x in range(1500):
            if distancee(x, y, circle[0], circle[1]) > circle[2] - 15 or distancee(x, y, circle[0], circle[1]) < 100: 
                image[y, x] = 0
    return image



def distancee(x1, y1, x2, y2):
    resultt = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return resultt