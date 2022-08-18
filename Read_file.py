# 读取文件函数

import h5py
import numpy as np


def get_stream(path):
    # 读取文件
    f = h5py.File(path)
    #遍历文件中的一级组
    for group in f.keys():
        # print("group = ",group)
        #根据一级组名获得其下面的组
        group_read = f[group]
        #遍历该一级组下面的子组
        for subgroup in group_read.keys():
            # 将不同的数据单独储存
            if subgroup == 'event_gs':
                dset = f[group+'/'+subgroup]
                event_gs_stream = dset[()]
            if subgroup == 'ts':
                dset = f[group+'/'+subgroup]
                ts_stream = dset[()]
            if subgroup == 'xs':
                dset = f[group+'/'+subgroup]
                xs_stream = dset[()]
            if subgroup == 'ys':
                dset = f[group+'/'+subgroup]
                ys_stream = dset[()]
    
    len = event_gs_stream.shape[0]
    array_stream = np.zeros((len, 4))
    array_stream[:, 0] = event_gs_stream
    array_stream[:, 1] = ts_stream
    array_stream[:, 2] = xs_stream
    array_stream[:, 3] = ys_stream
    array_stream = array_stream[10000000:10150000, :]
    print(array_stream.shape[0])
    return array_stream






