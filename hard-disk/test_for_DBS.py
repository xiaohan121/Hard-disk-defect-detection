# 判断DBS聚类函数

from numpy import unique
from numpy import where
from sklearn.cluster import DBSCAN
from matplotlib import pyplot
import copy
import numpy as np
import cv2

def image_findpoint(aaa):
    image = copy.deepcopy(aaa)
    a = []
    for y in range(800):
        for x in range(1500):
            if image[y, x] > 0: 
                a.append([x, y])
    a = np.array(a)
    return a            


def Dbs1(X):
    # 定义模型
    model = DBSCAN(eps=25.00, min_samples=5)
    # 模型拟合与聚类预测
    yhat = model.fit_predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
    pyplot.show()


def Dbs2(X):
    # 定义模型
    model = DBSCAN(eps=30.00, min_samples=10)
    # 模型拟合与聚类预测
    yhat = model.fit_predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
    pyplot.show()


def Dbs3(X):
    # 定义模型
    model = DBSCAN(eps=33.00, min_samples=10)
    # 模型拟合与聚类预测
    yhat = model.fit_predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
    pyplot.show()


def Dbs4(X):
    # 定义模型
    model = DBSCAN(eps=6.00, min_samples=2)
    # 模型拟合与聚类预测
    yhat = model.fit_predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
    pyplot.show()

image_discrete = cv2.imread('test/040_2_image_discrete_reimage.PNG')
image_discrete=cv2.cvtColor(image_discrete,cv2.COLOR_RGB2GRAY)
X = image_findpoint(image_discrete)
Dbs1(X)
Dbs2(X)
Dbs3(X)
Dbs4(X)
