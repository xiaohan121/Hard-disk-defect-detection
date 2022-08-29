# 引入三个函数

import numpy as np
import matplotlib.pyplot as plt
import Denoising
import Read_file
import Visualization
from Speed import speed
# import Time_correction


def dataset(data_path, label_path):
    data_path = './data_demo/001.h5'
    array_stream1, array_stream2 = Read_file.get_stream(data_path)
    label_path = './labels/001.txt'
    label = Read_file.get_label(label_path)
    label1 = np.zeros(5)
    label2 = np.zeros(5)
    array_stream1 = Denoising.denoising(array_stream1)
    speed1 = speed(array_stream1)
    image1, circle1 = Visualization.visualization(array_stream1, speed1)
    label1[0] = label[0]
    label1[1] = label[1] + circle1[0]
    label1[2] = label[2] + circle1[1]
    label1[3] = label[3]
    label1[4] = label[4]
    array_stream2 = Denoising.denoising(array_stream2)
    speed2 = speed(array_stream2)
    image2, circle2 = Visualization.visualization(array_stream2, speed2)
    label1[0] = label[0]
    label1[1] = label[1] + circle2[0]
    label1[2] = label[2] + circle2[1]
    label1[3] = label[3]
    label1[4] = label[4]
    return image1, image2, label1, label2
