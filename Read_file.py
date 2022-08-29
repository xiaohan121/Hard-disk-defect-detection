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
    start_1 = int(len / 4)
    end_1 = start_1 + 200000
    start_2 = int(len / 4 * 3)
    end_2 = start_2 + 200000
    array_stream1 = array_stream[start_1:end_1, :]
    array_stream2 = array_stream[start_2:end_2, :]
    return array_stream1, array_stream2


def get_label(path):
    data_list = []
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()
    for line in data:
        line = line.strip('\n')
        data_split = line.split(',')
        temp = list(map(float, data_split))
        data_list.append(temp)
    data_array = np.array(data_list)
    return data_array






