from Dataset import dataset
import os
import cv2

datas_path = './dataset/train/data'
labels_path = './dataset/train/label'
datas_file = os.listdir(datas_path)
labels_file = os.listdir(labels_path)
len = len(datas_file)
if os.path.exists('./data_set') == False:
    os.makedirs(r'./data_set/data')
    os.makedirs(r'./data_set/label')
for round in range(1):
    for i in range(len):
        i = i + 1
        print(i + round * len)
        data_file = datas_path + '/' + datas_file[i]
        label_file = labels_path + '/' + labels_file[i]
        image, label = dataset(data_file, label_file, round)
        name = str(round * len + i)
        cv2.imwrite('data_set/data/' + name + '.PNG', image)
        label_f = open('data_set/label/' + name + '.txt', 'w', encoding='utf_8')
        for j in range(label.shape[0]):
            for k in range(label.shape[1] - 1):
                label_f.write(str(int(label[j,k])) + ',')
            label_f.write(str(int(label[j,label.shape[1] - 1])))
            label_f.write('\n')
        label_f.close()

