
import Dataset

import matplotlib.pyplot as plt # plt 用于显示图片
import numpy as np
import algorithm_reimage
import cv2
import os

  

datas_path = './dataset/train/data'
labels_path = './dataset/train/label'
datas_file = os.listdir(datas_path)
labels_file = os.listdir(labels_path)
len = len(datas_file)
if os.path.exists('./data_set1') == False:
    os.makedirs(r'./data_set1/data')
    os.makedirs(r'./data_set1/data1')
    os.makedirs(r'./data_set1/label')

for i in range(len):
    # if i != 0:
        # continue
    data_file = datas_path + '/' + datas_file[i]
    label_file = labels_path + '/' + labels_file[i]
    kk = 0
    round = 0
    for z in range(9):
        image, image_continuous_mean, label, circles = Dataset.dataset(data_file, label_file, round)
        if  circles is None:
            round += 1
        else:
            circle1 = circles[0, 0]
            if circle1[0] <= 500:
                round += 2
            else:    
                label[:, 1] = label[:, 1] + circle1[0]
                label[:, 2] = 800 - int(label[:, 2] + circle1[1])
                image_continuous_mean = algorithm_reimage.reimage(image_continuous_mean, circle1)
                name = str(kk * len + i + 1)
                cv2.imwrite('data_set1/data/' + name + '.PNG', image)
                cv2.imwrite('data_set1/data1/' + name + '.PNG', image_continuous_mean)
                label_f = open('data_set1/label/' + name + '.txt', 'w', encoding='utf_8')
                for j in range(label.shape[0]):
                    for k in range(label.shape[1] - 1):
                        label_f.write(str(int(label[j,k])) + ',')
                    label_f.write(str(int(label[j,label.shape[1] - 1])))
                    label_f.write('\n')
                label_f.close()
                print(i + kk * len + 1)
                kk += 1
                round += 1
        if kk == 4:
            break
    print("已完成")

