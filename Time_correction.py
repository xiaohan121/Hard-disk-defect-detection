# 去噪函数

# 时间阈值设置 time_interval = 0.02
# 空间阈值设置 space_interval = 6

from turtle import speed
import numpy as np
import statistics

def speed_detection(array_stream):
    array_stream_new = np.zeros((1,4))
    time_dif = np.zeros((1,3))
    a = np.zeros((1,3))
    array_stream = array_stream[0:20000, :]
    length = array_stream.shape[0]
    for i in range(length):
        k = 0
        for j in range(max(0, i), min(i+2000, length)): # 正2000是为了控制检测的是时间范围大约在时间阈值里，减少要比对的数据量
            if j != i:
                if  array_stream[j][3] - array_stream[i][3] == 1 \
                    and array_stream[j][2] - array_stream[i][2] == 0 \
                    and abs(array_stream[j][0] - array_stream[i][0]) == 0 \
                    and abs(array_stream[j][1] - array_stream[i][1]) != 0: # 控制事件在一定的时间和空间范围内也有类似的事件发生才是好点
                    for z in range(3):
                        a[0][z] = array_stream[j][z + 1] - array_stream[i][z + 1]
                    k = 1
                    break
        if k == 1:
            array_stream_new = np.vstack((array_stream_new, array_stream[i,:]))
            time_dif = np.vstack((time_dif, a))
    speed = statistics.mode(time_dif[:, 0])
    print(speed)
    return speed

