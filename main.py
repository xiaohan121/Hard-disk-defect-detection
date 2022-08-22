# 引入三个函数
import Denoising
import Read_file
import Visualization
import Time_correction


path = './data_demo/004.h5'
array_stream = Read_file.get_stream(path)
speed = Time_correction.speed_detection(array_stream)
array_stream_new = Denoising.denoising(array_stream)
cricle = Visualization.visualization(array_stream_new, speed)
