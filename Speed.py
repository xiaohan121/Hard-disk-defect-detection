

import matplotlib.pyplot as plt # plt 用于显示图片
import numpy as np
import cv2 as cv
from Circle import circle

def speed(array_stream):
    length = array_stream.shape[0]
    list = np.arange(length)
    list1 = random_int(length)
    list2 = np.delete(list, list1)
    array_stream_new1 = array_stream[list1, :]
    array_stream_new2 = array_stream[list2, :]
    circle1 = circle(array_stream_new1, 0)
    circle2 = circle(array_stream_new2, 0)
    b = circle1[0] - circle2[0]
    speed = 0
    for j in range(560, 600):
        circle1 = circle(array_stream_new1, j)
        circle2 = circle(array_stream_new2, j)
        x = circle1[0] - circle2[0]
        if x < b:
            b = x
            speed = j
    return speed


def random_int(length):
    len = int(length / 2)
    print(len)
    list = np.random.rand(len)
    for i in range(len):
        list[i] = int(list[i] * length)
    list = np.unique(list)
    return list