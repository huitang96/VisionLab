'''
将voc转换为coco格式
首先将voc中的Annotations按照.txt的索引分为trainval训练集和test测试集
此脚本为分离训练集

'''

import os
import shutil

# the path is you original file directory
# the newpath is the new directory
class BatchCopy():
    def __init__(self):
        self.path = '/home/htang/proj/datasets/VOCdevkit/VOC2007/Annotations'
        self.newpath = '/home/htang/proj/datasets/VOCdevkit/VOC2007/train_annotations'

    def copy_file(self):
        filelist = os.listdir(self.path)  # file list in this directory
        # print(len(filelist))
        test_list = loadFileList()
        # print(len(test_list))
        for f in filelist:
            filedir = os.path.join(self.path, f)
            (shotname, extension) = os.path.splitext(f)
            if str(shotname) in test_list:
                # print('success')
                shutil.copyfile(str(filedir),os.path.join(self.newpath,f))
                

# load the list of train/test file list

#分离训练集和测试集索引

def loadFileList():
    filelist = []
    f = open("/home/htang/proj/datasets/VOCdevkit/VOC2007/ImageSets/Main/train.txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.strip('\r\n')  # to remove the '\n' for test.txt, '\r\n' for tainval.txt 
        line = str(line)
        filelist.append(line)
    f.close()
    # print(filelist)
    return filelist

if __name__ == '__main__':
    demo = BatchCopy()
    demo.copy_file()
    filelist = os.listdir('/home/htang/proj/datasets/VOCdevkit/VOC2007/train_annotations')
    # print(len(filelist))


