from cgi import print_arguments
import matplotlib.pyplot as plt # plt 用于显示图片
import numpy as np
import cv2 as cv

def visualization(array_stream, speed):
    image = np.zeros((800, 1580))
    len = array_stream.shape[0]
    print(len)
    for i in range(len):
        x = int(array_stream[i][3])
        y = int(array_stream[i][2] - (array_stream[i][1] - array_stream[0][1]) * speed) + 300
        image[x, y] += array_stream[i][0]
    plt.imshow(image, cmap='gray', origin='lower')
    plt.show()
    image = cv.medianBlur(np.uint8(image),5)
    circles = cv.HoughCircles(image,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=50,param2=30,minRadius=250,maxRadius=400)
    print(circles[0])
    return circles[0]