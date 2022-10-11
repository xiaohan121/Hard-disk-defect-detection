# 霍夫圆检测各种方法对比

import copy
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
    # plt.imshow(image, cmap='gray')
    # plt.title("input")
    # plt.show()
    cv.imshow('input', image)
    threshold_OTSU_method(image)
    threshold_triangle_method(image)
    mean_circles(image)
    row_method(image)
    mean_image(image)
    img = cv.medianBlur(np.uint8(image),3)
    # plt.imshow(img, cmap='gray')
    # plt.title("medianBlur")
    # plt.show()
    cv.imshow("median", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def row_method(aaa):
    image = copy.deepcopy(aaa)
    img = image.astype("uint8")
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=250,param2=35,minRadius=300,maxRadius=400)
    circles = np.uint16(np.around(circles))
    i = circles[0, 0]
    cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 在原图上画圆，圆心，半径，颜色，线框
    cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)  # 画圆心
    # plt.imshow(image, cmap='gray')
    # plt.title("row")
    # plt.show()
    cv.imshow('row', image)

def threshold_OTSU_method(aaa):
    image = copy.deepcopy(aaa)
    img = image.astype("uint8")
    th, dst = cv.threshold(img, 200, 255, cv.THRESH_BINARY + cv.THRESH_TRUNC + cv.THRESH_OTSU)
    circles = cv.HoughCircles(dst,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=50,param2=35,minRadius=300,maxRadius=400)
    circles = np.uint16(np.around(circles))
    i = circles[0, 0]
    cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 在原图上画圆，圆心，半径，颜色，线框
    cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)  # 画圆心
    # plt.imshow(image, cmap='gray')
    # plt.title("otsu")
    # plt.show()
    cv.imshow('otsu', image)

def threshold_triangle_method(aaa):
    image = copy.deepcopy(aaa)
    img = image.astype("uint8")
    th, dst = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)
    circles = cv.HoughCircles(dst,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=50,param2=15,minRadius=300,maxRadius=400)
    circles = np.uint16(np.around(circles))
    i = circles[0, 0]
    cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 在原图上画圆，圆心，半径，颜色，线框
    cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)  # 画圆心
    # plt.imshow(image, cmap='gray')
    # plt.title("tri")
    # plt.show()
    cv.imshow('tri', image)

def mean_circles(aaa):
    image = copy.deepcopy(aaa)
    img = cv.medianBlur(np.uint8(image),5)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,dp=1,minDist=100,param1=100,param2=35,minRadius=300,maxRadius=400)
    circles = np.uint16(np.around(circles))
    i = circles[0, 0]
    cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 在原图上画圆，圆心，半径，颜色，线框
    cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)  # 画圆心
    # plt.imshow(image, cmap='gray')
    # plt.title("mean")
    # plt.show()
    cv.imshow('mean', image)

def mean_image(aaa):
    image = copy.deepcopy(aaa)
    mean = 0
    k = 0
    for y in range(800):
        for x in range(1380):
            if image[y, x] > 0:
                mean += image[y, x]
                k += 1
    mean = mean / k
    print(mean)
    for y in range(800):
        for x in range(1380):
            if image[y, x] >= mean:
                image[y, x] = 1
            else:
                image[y, x] = 0
    cv.imshow("ddd", image)
