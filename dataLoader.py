# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:06:10 2022

@author: zhaodi
"""

import h5py
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

from evalFun import evalFunction

class dataLoader():
    def __init__(self):
        pass
        self.array_stream = None
        self.path = ''
        self.stream = {'event_gs':[], 'ts':[], 'xs':[], 'ys':[]}
        
    def getStream(self, path):
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
                self.stream[subgroup] = f[group+'/'+subgroup][()]
        
        self.length = self.stream['event_gs'].shape[0]
        self.array_stream = np.zeros((self.length, 4))
        
        for i, keys in enumerate(self.stream.keys()):
            self.array_stream[:,i] = self.stream[keys]
        return self.stream
        # array_stream = array_stream[10000000:10100000, :]
        # array_stream = array_stream[:, :]
        
    def imaging(self, clipsLen, v, skiprows):
        if type(self.array_stream) != np.ndarray:
            self.getStream(self.path)
        self.image = np.zeros((800, 1800))
        for i in (self.array_stream[skiprows : skiprows+clipsLen]):
            x = int(i[3])
            y = int(i[2] - (i[1] - self.array_stream[skiprows,1]) * -v)
            self.image[x, y] += i[0]
            # print((i[1] - self.array_stream[skiprows,1]) * -v)
            
        # if ch == None:
        #     ch = round(self.length/clipsLen + 0.5)
        # self.image = np.zeros((800, 6000, ch))
        # # print(len)
        # for c in tqdm(range(ch)):
        #     for i in (self.array_stream[c*clipsLen:(c+1)*clipsLen,:]):
        #         x = int(i[3])
        #         # y = int(i[2])
        #         y = int(i[2] - (i[1] - self.array_stream[0,1]) * v)
        #         self.image[x, y, c] += i[0]
        #         # print(x)

        return self.image


#%%
if __name__ == '__main__' :
    path = 'E:/PCBDDData/Hard-disk-defect-detection/dataset/dataset/train/data/003.h5'
    loader = dataLoader()
    evalF = evalFunction()
    stream = loader.getStream(path)
    # for v in range(-1000,1000):   
    #     image = loader.imaging(clipsLen = 1000000, v = -5.9e2, skiprows = 10000000)
    # plt.imshow(image, cmap = 'gray')
    #%%
    methods = ['Brenner', 'Tenengrad', 'Laplacian', 'SMD', 'SMD2', 'Var', 'eGrad', 'Vollath']
    resultAll = {'Brenner':[], 'Tenengrad':[], 'Laplacian':[], 'SMD':[], 'SMD2':[], 'Var':[], 'eGrad':[], 'Vollath':[]}
    
    # plt.figure()
    baseV = 590
    ran = [-30,10]
    for v in tqdm(range(ran[0],ran[1])):
        img = loader.imaging(clipsLen = 1000000, v = baseV + v, skiprows = 5500000)
        # plt.subplot(7,3,v+11)
        # plt.figure()
        # plt.imshow(img, cmap = 'gray')
        evalF.loadImg(img)
        res = evalF.qualityEval( methods = methods)
        for m in methods:
            resultAll[m].append(res[m])
            
    plt.figure()
    resV = []
    for m in methods:
        plt.plot(range(baseV+ran[0],baseV+ran[1]), resultAll[m]/max(resultAll[m]))
        resV.append(np.argmax(resultAll[m]))
    plt.legend(methods)
    
    v = baseV+ran[0]+np.mean(resV)
    print(v)
    
    plt.figure()
    plt.imshow(loader.imaging(clipsLen = 1000000, v = v, skiprows = 5500000), cmap = 'gray')
    
    # plt.figure()
    # plt.imshow(loader.imaging(clipsLen = 1000000, v = 590, skiprows = 10000000) - loader.imaging(clipsLen = 1000000, v = 580, skiprows = 10000000), cmap = 'gray')
    
    
    