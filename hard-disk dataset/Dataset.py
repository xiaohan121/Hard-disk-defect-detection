# 引入三个函数

import numpy as np
import Denoising
import Read_file
import Visualization
from Speed import speed
# import Time_correction


def dataset(data_path, label_path, round):
    
    array_stream = Read_file.get_stream(data_path, round)
    label = Read_file.get_label(label_path)
    array_stream = Denoising.denoising(array_stream)
    spd = speed(array_stream)
    image, circle = Visualization.visualization(array_stream, spd)
    label[:, 1] = label[:, 1] + circle[0]
    label[:, 2] = label[:, 2] + circle[1]

    
    return image, label
