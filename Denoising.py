time_interval = 0.02
space_interval = 6


import numpy as np


def denoising(array_stream, time_interval = 0.02, space_interval = 6):
    array_stream_new = np.zeros((1,4))
    length = array_stream.shape[0]
    for i in range(length):
        print(i)
        k = 0
        for j in range(max(0, i-2000), min(i+2000, length)):
            if j != i:
                if ((abs(array_stream[i][2] - array_stream[j][2]) + abs(array_stream[i][3] - array_stream[j][3])) <= space_interval ) \
                    and abs(array_stream[i][1] - array_stream[j][1]) <= time_interval:
                    k = 1
                    break
        if k == 1:
            array_stream_new = np.vstack((array_stream_new, array_stream[i,:]))
            print("好点")
        else:
            print("噪音")
                
    return array_stream_new