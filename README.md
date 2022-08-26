# Hard-disk-defect-detection
## 通过清晰度指标进行速度标定

### 评估函数
- [x] Brenner、Tenengrad、Laplacian、SMD、SMD2、Var、eGrad、Vollath
- [ ] infEntropy、EAV、Reblur、NRSS、Fourier

### 测试结果

在 560-600 范围内进行搜索，各个清晰度指标如图

![resLine](https://user-images.githubusercontent.com/69668611/186872649-9d4a0095-5d63-4df9-ba3c-2fb82d8fce68.png)

速度计算结果为各个指标峰值点均值 573.25

![标定结果](https://user-images.githubusercontent.com/69668611/186872991-8062a230-0e51-41f2-be63-bf83d94dbbae.png)

### 待办事项
- [ ] 设计更好的搜索方式计算速度
- [ ] 由于同一文件内速度多次变化，所以应当设计合理的数据分段方式
