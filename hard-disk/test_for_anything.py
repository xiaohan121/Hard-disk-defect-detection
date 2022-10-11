# 判断聚类函数

from numpy import unique
from numpy import where
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
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


def Aff(X):
    # 定义模型
    model = AffinityPropagation(damping=0.9)
    # 匹配模型
    model.fit(X)
    # 为每个示例分配一个集群
    yhat = model.predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
    pyplot.gca().invert_yaxis()
    pyplot.show()

def Dbs(X):
    # 定义模型
    model = DBSCAN(eps=32.00, min_samples=10)
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
    pyplot.gca().invert_yaxis()
    pyplot.show()

def Kmean(X):
    # 定义模型
    model = KMeans(n_clusters=3)
    # 模型拟合
    model.fit(X)
    # 为每个示例分配一个集群
    yhat = model.predict(X)
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
    pyplot.gca().invert_yaxis()
    pyplot.show()

def Meanshift(X):
    # 定义模型
    model = MeanShift()
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
    pyplot.gca().invert_yaxis()
    pyplot.show()


image_discrete = cv2.imread('test/010_2_image_continuous_mean_reimage.PNG')
image_discrete=cv2.cvtColor(image_discrete,cv2.COLOR_RGB2GRAY)
X = image_findpoint(image_discrete)
# Aff(X)
# Dbs(X)
# Kmean(X)
Meanshift(X)