
from turtle import speed
import matplotlib.pyplot as plt # plt 用于显示图片
import numpy as np
import cv2 as cv

def visualization(array_stream, speed):
    image = np.zeros((800, 1380))
    len = array_stream.shape[0]
    for i in range(len):
        y = int(array_stream[i][3])
        x = int((array_stream[i][2]) - (array_stream[i][1] - array_stream[0][1]) * speed + 100)
        image[y, x] += array_stream[i][0]
    plt.imshow(image, cmap='gray')
    plt.show()
    img = cv.medianBlur(np.uint8(image),3)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=100,param2=35,minRadius=250,maxRadius=400)
    # print(circles[0, 0])
    return image, circles[0, 0]