

## RFNet: Toward High-Quality Object Detection in Aerial Images  
### 拟解决的问题
用于解决航拍场景中，目标检测的误检与漏检等问题  
### 解决方案
1：以Cascade R-CNN 为基准基础，在特征金字塔结构（PAFPN）中引入递归特征融合的回路【命令为RFNet】  
2：引入注意力机制到ResNet中进行特征的提取  
3：并将最近邻插值法二倍上采样替换为基于深度学习的上采样（CARAFE）的融合方法  
### 实验结果
mAP平均精度指标提高1.1%，中尺寸目标精度提高2.1%，卡车类别的单类精度提高2.4%，其它类别检测均有所不同程度的提高  
### 不足
1：网络的改进与上采样方法的替换没有进行消融实验，难以证明精度的提升是网络的改进带来的  
2：论文中实验的动机相关的表述有所不足  
3：网络结构的原理表述相对空洞，对t次循环的探索相对模糊，对网络内在性能和原理表述有所缺陷  
### 改进
1：对FPN结构进行优化，展开对语义分割的探索  
2：结合CVPR2022卷积方式，设计空洞卷积结合递归RFNet进行进一步改进  
（2022.4.22）  

## 实验
环境：
cuda-11.0  cudnn-8.0  pytorch-1.8  
[docker](www.baidu.com)  
MSCOCO 2014  |  PASCAL VOC07+12  
Cascade R-CNN - Object Detection + Instance Segmataion

[复现指南](https://github.com/ruoqianguo/cascade-rcnn_Pytorch)  
