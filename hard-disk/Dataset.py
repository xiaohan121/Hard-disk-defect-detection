# 数据集准备

import algorithm_data_denoising
import algorithm_read_file
import algorithm_new_image
import copy

from algorithm_speed import speed
import cv2


def dataset(data_path, label_path, round):
    array_stream = algorithm_read_file.get_stream(data_path, round)
    label = algorithm_read_file.get_label(label_path)
    array_stream = algorithm_data_denoising.denoising(array_stream)
    spd = speed(array_stream)
    image_continuous, image_continuous_mean = algorithm_new_image.visualization_continuous(array_stream, spd)
    circles = row_method(image_continuous)

    return image_continuous, image_continuous_mean, label, circles



def row_method(aaa):
    image = copy.deepcopy(aaa)
    img = image.astype("uint8")
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp=1,minDist=100,param1=250,param2=35,minRadius=300,maxRadius=400)
    
    return circles