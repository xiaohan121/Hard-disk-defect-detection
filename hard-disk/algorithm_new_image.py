# 图像去噪函数

import copy
import numpy as np
import cv2 as cv

def visualization_discrete(array_stream, speed):
    image = np.zeros((800, 1500))
    len = array_stream.shape[0]
    for i in range(len):
        y = int(array_stream[i][3])
        x = int((array_stream[i][2]) - (array_stream[i][1] - array_stream[0][1]) * speed + 220)
        image[y, x] += array_stream[i][0]
    # plt.imshow(image, cmap='gray')
    # plt.title("input")
    # plt.show()
    # cv.imshow('input_discrete', image)

    a = mean_image(image, 0.9)
    # cv.imshow("mean_discrete", a)

    # image_uint8 = image.astype("uint8")

    '''
    th, dst = cv.threshold(image_uint8, 200, 255, cv.THRESH_BINARY + cv.THRESH_TRUNC + cv.THRESH_OTSU)
    cv.imshow("threshold, 200, binary+trunc+otsu", dst)

    th, dst = cv.threshold(image_uint8, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)
    cv.imshow("threshold, 0, binary+triangle", dst)

    image_median_3 = cv.medianBlur(image_uint8,3)
    cv.imshow("median, 3", image_median_3)

    image_median_5 = cv.medianBlur(image_uint8,5)
    cv.imshow("median, 5", image_median_5)
    '''

    # plt.imshow(img, cmap='gray')
    # plt.title("medianBlur")
    # plt.show()

    a_uint8 = image.astype("uint8")
    # cv.imshow("mean_uint8", a)
    
    b = cv.medianBlur(a_uint8,3)
    # cv.imshow("mean + median", b)

    return a, b


def visualization_continuous(array_stream, speed):
    image = np.zeros((800, 1500))
    len = array_stream.shape[0]
    for i in range(len):
        y = int(array_stream[i][3])
        x = int((array_stream[i][2]) - (array_stream[i][1] - array_stream[0][1]) * speed + 220)
        image[y, x] += array_stream[i][0]
    # plt.imshow(image, cmap='gray')
    # plt.title("input")
    # plt.show()
    # cv.imshow('input_continuous', image)

    a = mean_image(image, 1.25)
    # cv.imshow("mean_continuous", a)

    # image_uint8 = image.astype("uint8")

    '''
    th, dst = cv.threshold(image_uint8, 200, 255, cv.THRESH_BINARY + cv.THRESH_TRUNC + cv.THRESH_OTSU)
    cv.imshow("threshold, 200, binary+trunc+otsu", dst)

    th, dst = cv.threshold(image_uint8, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)
    cv.imshow("threshold, 0, binary+triangle", dst)

    image_median_3 = cv.medianBlur(image_uint8,3)
    cv.imshow("median, 3", image_median_3)

    image_median_5 = cv.medianBlur(image_uint8,5)
    cv.imshow("median, 5", image_median_5)
    '''

    # plt.imshow(img, cmap='gray')
    # plt.title("medianBlur")
    # plt.show()

    # a_uint8 = image.astype("uint8")
    # b = cv.medianBlur(a_uint8,3)
    # cv.imshow("mean + median", b)
    
    return image, a



def mean_image(aaa, a):
    image = copy.deepcopy(aaa)
    mean = 0
    k = 0
    z = 0
    for y in range(800):
        for x in range(1500):
            if image[y, x] > 0:
                mean += image[y, x]
                k += 1
    mean = mean / k
    # print(mean, k)
    for y in range(800):
        for x in range(1500):
            if image[y, x] >= a * mean:
                image[y, x] = 255
                z += 1
            else:
                image[y, x] = 0
    # print(z)
    return image

def mean_image_uint8(aaa, a):
    image = copy.deepcopy(aaa)
    mean = 0
    k = 0
    z = 0
    for y in range(800):
        for x in range(1500):
            if image[y, x] > 0:
                mean += image[y, x]
                k += 1
    mean = mean / k
    # print(mean, k)
    for y in range(800):
        for x in range(1500):
            if image[y, x] >= a * mean:
                image[y, x] = 255
                z += 1
            else:
                image[y, x] = 0
    # print(z)
    return image