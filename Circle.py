
import matplotlib.pyplot as plt # plt 用于显示图片
import numpy as np
import cv2 as cv

def circle(array_stream, j):
    image = np.zeros((800, 1380))
    len = array_stream.shape[0]
    for i in range(len):
        y = int(array_stream[i][3])
        x = int((array_stream[i][2]) - (array_stream[i][1] - array_stream[0][1]) * j + 100)
        image[y, x] += array_stream[i][0]
    # plt.imshow(image, cmap='gray')
    # plt.show()
    image = cv.medianBlur(np.uint8(image),3)
    circles = cv.HoughCircles(image,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=100,param2=25,minRadius=300,maxRadius=400)
    # print(circles[0, 0])
    return circles[0, 0]