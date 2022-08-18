# 引入三个函数
import Denoising
import Read_file
import Visualization


path = './data_demo/003.h5'
array_stream = Read_file.get_stream(path)
array_stream_new = Denoising.denoising(array_stream)
Visualization.visualization(array_stream_new)
