# 图像运动速度判定函数

import numpy as np
from algorithm_smd import T_img

def speed(array_stream):
    t_image = T_img(array_stream, 0)
    b = t_image
    speed = 0
    for j in range(480, 620):
        t_image = T_img(array_stream, j)
        x = t_image
        if x > b:
            b = x
            speed = j
    return speed