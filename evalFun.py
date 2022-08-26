# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 10:44:01 2022

@author: zhaodi
"""

import os
import cv2
import torch
import numpy as np
import kornia as K
import matplotlib.pyplot as plt

from tqdm import tqdm

def file_name(file_dir, fileType = '.bmp'):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == fileType:  
                L.append(os.path.join(root, file))
    return L


class evalFunction():
    def __init__(self):
        
        self.ROI = [[150,8000],[4700,7100]]
        self.img = None
        self.funs = {'Brenner': self.Brenner,'Tenengrad': self.Tenengrad,
                     'Laplacian': self.Laplacian,'SMD': self.SMD,
                     'SMD2': self.SMD2,'Var': self.Var,
                     'eGrad': self.eGrad,'Vollath': self.Vollath,
                     'infEntropy': self.infEntropy,'EAV': self.EAV,
                     'Reblur': self.Reblur,'NRSS': self.NRSS,
                     'Fourier': self.Fourier}
        
    def loadImg(self, img):
        self.imgTensor: torch.tensor = K.image_to_tensor(img).cuda() # CxHxW / torch.uint8
        self.imgTensor: torch.tensor = self.imgTensor.unsqueeze(0)+0.0  # 1xCxHxW
    
    def qualityEval(self, methods = ['Brenner'], withGrad = 0):
        # self.loadImg(path)
        self.res = {}
        for m in methods:
            if withGrad != 1:
                self.res[m] = self.funs[m]().cpu().numpy().astype(np.float32) + 0
            else:
                self.res[m] = self.funs[m]()
        return self.res
    
    def Brenner(self):
        return ((self.imgTensor[0,:,1:,:] - self.imgTensor[0,:,:-1,:])**2).sum()
    
    def Tenengrad(self):
        sobelResTensor = K.filters.spatial_gradient(self.imgTensor, mode='sobel', order=1, normalized=True)
        sobelX = sobelResTensor[:,:,0,:,:]
        sobelY = sobelResTensor[:,:,1,:,:]
        return (sobelX**2 + sobelY**2).sqrt().sum()
    
    def Laplacian(self):
        laplacianResTensor = K.filters.laplacian(self.imgTensor, kernel_size=3)
        return (laplacianResTensor).abs().sum()
    
    def SMD(self):
        dx = (self.imgTensor[0,:,1:,:] - self.imgTensor[0,:,:-1,:]).abs().sum()
        dy = (self.imgTensor[0,:,:,1:] - self.imgTensor[0,:,:,:-1]).abs().sum()
        return dx+dy
    
    def SMD2(self):
        dx = (self.imgTensor[0,:,1:,:-1] - self.imgTensor[0,:,:-1,:-1]).abs()
        dy = (self.imgTensor[0,:,1:,1:] - self.imgTensor[0,:,1:,:-1]).abs()
        
        return (dx*dy).sum()
    
    def Var(self):
        return self.imgTensor.var()
    
    def eGrad(self):
        dx = ((self.imgTensor[0,:,1:,:] - self.imgTensor[0,:,:-1,:])**2).sum()
        dy = ((self.imgTensor[0,:,:,1:] - self.imgTensor[0,:,:,:-1])**2).sum()
        return dx+dy
    
    def Vollath(self):
        vx = (self.imgTensor[0,:,1:,:] * self.imgTensor[0,:,:-1,:]).sum()
        v = vx - (self.imgTensor.numel() * self.imgTensor.mean()**2)
        return v

    def crop():
        # TODO
        pass

    def infEntropy(self):
        # TODO
        return -1
    def EAV(self):
        # TODO
        return -1
    def Reblur(self):
        # TODO
        return -1
    def NRSS(self):
        # TODO
        return -1
    def Fourier(self):
        # TODO
        return -1

if __name__ == '__main__' :
    test = evalFunction()
    path = 'D:/PCBDD/AutoFocusDataSet/2/'
    files = file_name(path, fileType = '.bmp')
    methods = ['Brenner', 'Tenengrad', 'Laplacian', 'SMD', 'SMD2', 'Var', 'eGrad', 'Vollath']
    resultAll = {'Brenner':[], 'Tenengrad':[], 'Laplacian':[], 'SMD':[], 'SMD2':[], 'Var':[], 'eGrad':[], 'Vollath':[]}
    
    for file in tqdm(files):
        test.loadImg(file)
        res = test.qualityEval( methods = methods)
        for m in methods:
            resultAll[m].append(res[m])
    plt.figure()
    for m in methods:
        # plt.figure()
        plt.plot(resultAll[m]/max(resultAll[m]))
        # plt.scatter(resultAll[m].index(max(resultAll[m])),1)
        # plt.title(m)
    plt.legend(methods)
    
# x_sobel: torch.Tensor = K.filters.sobel(test.imgRGBTensor)
# plt.figure()
# plt.imshow(1-x_sobel[0,0,:,:].cpu(), cmap = 'gray')



# x_laplacian: torch.Tensor = K.filters.canny(test.imgRGBTensor)[0]
# plt.figure()
# plt.imshow(1-x_sobel[0,0,:,:].cpu(), cmap = 'gray')
