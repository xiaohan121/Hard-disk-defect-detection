# 去噪函数

# 时间阈值设置 time_interval = 0.02
# 空间阈值设置 space_interval = 6

import numpy as np


def denoising(array_stream, time_interval = 0.01, space_interval = 5):
    array_stream_new = np.zeros((1,4))
    length = array_stream.shape[0]
    for i in range(length):
        # print(i)
        k = 0
        for j in range(max(0, i), min(i+2000, length)): # 正负2000是为了控制检测的是时间范围大约在时间阈值里，减少要比对的数据量
            if j != i:
                if ((abs(array_stream[i][2] - array_stream[j][2]) + abs(array_stream[i][3] - array_stream[j][3])) <= space_interval ) \
                    and abs(array_stream[i][1] - array_stream[j][1]) <= time_interval: # 控制事件在一定的时间和空间范围内也有类似的事件发生才是好点
                    k = 1
                    break
        if k == 1:
            array_stream_new = np.vstack((array_stream_new, array_stream[i,:]))
            # print("好点")
        # else:
            # print("噪音")
                
    return array_stream_new