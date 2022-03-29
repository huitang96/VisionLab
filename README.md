# VISION LAB
Include Writing and InPlement
                                              ![image](https://github.com/huitang96/PaperList-2D/blob/master/images/Welcome%20(1).png)  
                                                                                                                                                      Tang Hui [CV](https://github.com/huitang96/PaperList-2D/blob/master/images/cv.pdf)  
## *WebSite*
[Nature Machine Intelligence ](https://www.nature.com/natmachintell/)

## *DataBASE*
[PQDT](http://www-pqdtcn-com-s.vpn.cdut.edu.cn:8118/)  
[Web of Science](http://www-webofscience-com-s.vpn.cdut.edu.cn:8118/wos/alldb/basic-search)  
[SciHub](https://sci-hub.st/)  
[CVPR/ECCV 2020-2022](https://sci-hub.st/)
## *Recently work*  
*Convolution Scheme*:  
*Feature Pyramid Network*:  
*Multi-Scale Dilation Convoluton*:  

## *2D Object Detection PaperL*
#### 1998  
*LeNet-5*: Gradient-Based Learning Applied to Document Recognition ([PDF](https://sci-hub.st/10.1109/5.726791))  
*CITE*: LeCun Y, Bottou L, Bengio Y,et al. Gradient-based learning applied to document recognition. 1998, 86(11):2278-324.  
*ABSTART*: 1998年，LeCun Y等人设计了5层的卷积神经网络LeNet-5并用于银行支票2D手写字体识别，取得较好的实用价值  
#### 2012
**AlexNet**: ImageNet Classification with Deep Convolutional Neural Networks ([PDF12](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) [PDF17](https://sci-hub.st/10.1145/3065386))  
**CITE**: Krizhevsky A, Sutskever I, Hinton GE. Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems. 2012;25.  
**ABSTRAT**: 2012年，Hinton课题组将深度学习方法引入图像识别，设计了卷积神经网络AlexNet用于ImageNet1000个类别的大规模图像识别，在当时取得了显著优于其它识别算法的效果。  
#### 2014  
**R-CNN**: Rich feature hierarchies for accurate object detection and semantic segmentation  ([PDF2](https://arxiv.org/pdf/1311.2524v5.pdf))  
**CITE**: Girshick R, Donahue J, Darrell T, Malik J. Rich feature hierarchies for accurate object detection and semantic segmentation. IEEE conference on computer vision and pattern recognition. 2014, 580-587.  
**ABSTART**: 2014年，Girshick R等人通过设计卷积神经网络CNN用于提取目标的特征，最后用于目标检测和语义分割，结果表明显著的优于OverFeat方法  
1、训练分多步：R-CNN的训练先要fine tuning一个预训练的网络，然后针对每个类别都训练一个SVM分类器，最后还要用regressors对bounding-box进行回归，另外region proposal也要单独用selective search的方式获得，步骤比较繁琐  
2、时间和内存消耗比较大。在训练SVM和回归的时候需要用网络训练的特征作为输入，特征保存在磁盘上再读入的时间消耗还是比较大的  
3、测试的时候也比较慢，每张图片的每个region proposal都要做卷积，重复操作太多  

#### 2015  
**Fast R-CNN**: Fast R-CNN ([PDF](https://arxiv.org/pdf/1504.08083.pdf)  
**CITE**: Girshick R. Fast r-cnn. IEEE international conference on computer vision. 2015, 1440-1448.  
**ABSTRACT**: Girshick R在R-CNN的基础上，  
1、卷积不再是对每个region proposal进行，而是直接对整张图像，这样减少了很多重复计算。原来RCNN是对每个region proposal分别做卷积，因为一张图像中有2000左右的region proposal，肯定相互之间的重叠率很高，因此产生重复计算  
2、用ROI pooling进行特征的尺寸变换，因为全连接层的输入要求尺寸大小一样，因此不能直接把region proposal作为输入  
3、将regressor放进网络一起训练，每个类别对应一个regressor，同时用softmax代替原来的SVM分类器  

## *Related Research*  
**CARAFE**: CARAFE: Content-Aware ReAssembly of FEatures ([PDF](https://arxiv.org/pdf/1905.02188.pdf))  
**CITE**: Wang J, Chen K, Xu R, Liu Z, Loy CC, Lin D. Carafe: Content-aware reassembly of features. IEEE/CVF International Conference on Computer Vision. 2019, 3007-3016.   
