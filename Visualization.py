import matplotlib.pyplot as plt # plt 用于显示图片
import numpy as np


def visualization(array_stream):
    image = np.zeros((800, 1280))
    len = array_stream.shape[0]
    print(len)
    for i in range(len):
        x = int(array_stream[i][3])
        y = int(array_stream[i][2])
        image[x, y] = array_stream[i][0]
    plt.imshow(image, cmap='gray', origin='lower')
    plt.show()
    return 0