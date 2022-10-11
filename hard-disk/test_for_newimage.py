import algorithm_data_denoising
import algorithm_read_file
import algorithm_new_image
import cv2
from algorithm_speed import speed

data_path = 'dataset/train/data/001.h5'
label_path = 'dataset/train/label/001.txt'
round = 2


def dataset(data_path, label_path, round):
    array_stream1, array_stream2 = algorithm_read_file.get_stream(data_path, round)
    label = algorithm_read_file.get_label(label_path)
    array_stream1 = algorithm_data_denoising.denoising(array_stream1)
    array_stream2 = algorithm_data_denoising.denoising(array_stream2)
    spd1 = speed(array_stream1)
    spd2 = speed(array_stream2)
    image_discrete, image_discrete_median = algorithm_new_image.visualization_discrete(array_stream1, spd1)
    image_continuous, image_continuous_mean = algorithm_new_image.visualization_continuous(array_stream2, spd2)
    cv2.imshow('input_discrete_mean', image_discrete)
    cv2.imshow("discrete_median", image_discrete_median)
    cv2.imshow("input_continuous", image_continuous)
    cv2.imshow("continuous_mean", image_continuous_mean)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
dataset(data_path, label_path, round)
