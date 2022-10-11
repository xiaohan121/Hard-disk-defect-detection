# 图像清晰度函数

import numpy as np

def T_img(array_stream, j):
    image = np.zeros((800, 1500))
    len = array_stream.shape[0]
    for i in range(len):
        y = int(array_stream[i][3])
        x = int((array_stream[i][2]) - (array_stream[i][1] - array_stream[0][1]) * j + 100)
        image[y, x] += array_stream[i][0]
    # plt.imshow(image, cmap='gray')
    # plt.show()
    T_image = variance(image)
    # print(circles[0, 0])
    return T_image

def variance(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像约清晰越大
    '''
    out = 0
    u = np.mean(img)
    shape = np.shape(img)
    for x in range(0,shape[0]):
        for y in range(0,shape[1]):
            out+=(img[x,y]-u)**2
    return out
