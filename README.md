<p align="center">
VISION LAB
</p>

## *WebSite*
[Nature Machine Intelligence ](https://www.nature.com/natmachintell/)
## *Scholar Research*
[HeKaiming](https://scholar.google.com/citations?hl=zh-CN&user=DhtAFkwAAAAJ&view_op=list_works&sortby=pubdate)   
[RossGirshick](https://scholar.google.com/citations?hl=zh-CN&user=W8VIEZgAAAAJ&view_op=list_works&sortby=pubdate)  
[ChenKai](https://scholar.google.com/citations?hl=zh-CN&user=eGD0b7IAAAAJ&view_op=list_works&sortby=pubdate)  
[Sunjian](https://scholar.google.com/citations?hl=zh-CN&user=ALVSZAYAAAAJ&view_op=list_works&sortby=pubdate)  
[Jitendra Malik](https://scholar.google.com/citations?hl=zh-CN&user=oY9R5YQAAAAJ&view_op=list_works&sortby=pubdate)  
## *DataBASE*
[PQDT](http://www-pqdtcn-com-s.vpn.cdut.edu.cn:8118/)  
[Web of Science](http://www-webofscience-com-s.vpn.cdut.edu.cn:8118/wos/alldb/basic-search)  
[SciHub](https://sci-hub.st/)  
[CVPR/ECCV 2020-2022](https://sci-hub.st/)
## *Windows*
[Wechat](https://mp.weixin.qq.com/cgi-bin/loginpage?url=%2Fcgi-bin%2Facctclose%3Faction%3Dpage%26token%3D59894322%26lang%3Dzh_CN)  
[Douyin](https://ID:AILAB)  
[Company](https://xxx)
## *Research Interests*  
*Computer Vision*  
*Machine Learning*  
## *Publication*  
[目标检测技术-Pytorch实现](https://xxx)  
## *2D Object Detection PaperL*
#### 1998  
**LeNet-5**: Gradient-Based Learning Applied to Document Recognition ([PDF](https://sci-hub.st/10.1109/5.726791))  
**Abstract:** 1998年，LeCun Y等人设计了5层的卷积神经网络LeNet-5并用于银行支票2D手写字体识别，取得较好的实用价值  
#### 2012
**AlexNet**: ImageNet Classification with Deep Convolutional Neural Networks ([PDF12](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) [PDF17](https://sci-hub.st/10.1145/3065386))  
**Abstract:** 2012年，Hinton课题组将深度学习方法引入图像识别，设计了卷积神经网络AlexNet用于ImageNet1000个类别的大规模图像识别，在当时取得了显著优于其它识别算法的效果。  
#### 2014  
**R-CNN**: Rich feature hierarchies for accurate object detection and semantic segmentation  ([PDF2](https://arxiv.org/pdf/1311.2524v5.pdf))  
**Abstract:** 2014年，Girshick R等人通过设计卷积神经网络CNN用于提取目标的特征，最后用于目标检测和语义分割，结果表明显著的优于OverFeat方法  
1、训练分多步：R-CNN的训练先要fine tuning一个预训练的网络，然后针对每个类别都训练一个SVM分类器，最后还要用regressors对bounding-box进行回归，另外region proposal也要单独用selective search的方式获得，步骤比较繁琐  
2、时间和内存消耗比较大。在训练SVM和回归的时候需要用网络训练的特征作为输入，特征保存在磁盘上再读入的时间消耗还是比较大的  
3、测试的时候也比较慢，每张图片的每个region proposal都要做卷积，重复操作太多  
#### 2015  
**Fast R-CNN**: Fast R-CNN ([PDF](https://arxiv.org/pdf/1504.08083.pdf))  
**Abstract:** Girshick R在R-CNN的基础上，  
1、卷积不再是对每个region proposal进行，而是直接对整张图像，这样减少了很多重复计算。原来RCNN是对每个region proposal分别做卷积，因为一张图像中有2000左右的region proposal，肯定相互之间的重叠率很高，因此产生重复计算  
2、用ROI pooling进行特征的尺寸变换，因为全连接层的输入要求尺寸大小一样，因此不能直接把region proposal作为输入  
3、将regressor放进网络一起训练，每个类别对应一个regressor，同时用softmax代替原来的SVM分类器  

**Faster R-CNN**Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks  
**Abstract:** 
## *Related Research*  
**CARAFE**: CARAFE: Content-Aware ReAssembly of FEatures ([PDF](https://arxiv.org/pdf/1905.02188.pdf))  
****
## *SUBMIT*  
|Journal/Conference|classes|SubmissionTime|Notes|Wesite
|---|---|---|---|---
|IEEE Signal Processing Letter(SPL)|JCR-2,IF=3.1|2 Months|Writing Skills and Mathematical principles|[official](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=97)  [Letpub](http://www.letpub.com.cn/index.php?page=journalapp&view=detail&journalid=3353)  
|传感器与微系统|中文核心,CSCD|10天|原理清晰,实验充足|[official](https://cgqj.cbpt.cnki.net/WKE2/WebPublication/index.aspx?mid=CGQJ)  
|模式识别与人工智能|EI|待了解| |[official](http://manu46.magtech.com.cn/Jweb_prai/CN/volumn/home.shtml)  
****
## *BOOKS and Mertials*  
****
[CSCD中文期刊](https://github.com/huitang96/PaperList-2D/blob/master/Resource/CSCD%E6%9C%9F%E5%88%8A%E7%9B%AE%E5%BD%95.pdf)
****
