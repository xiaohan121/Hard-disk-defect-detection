# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:10:02 2022

@author: zhaodi
"""

import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from evalFun import evalFunction
from dataLoader import dataLoader
#%%
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