import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2 as cv
import numpy as np
import random

np.set_printoptions(threshold=np.inf)
IMG_SHAPE = 56

Samplesize = 2000
TestS = 150

samplelist = ['0','1','2','3','4','5','6','7','8','9']
testnum = 0

def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 2.5)
    cv.bitwise_not(binary,binary)
    return binary


def gettest_char():
    filepath = "C:/Users/JarvisZhang/Desktop/tmp/Test"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((TestS*len(samplelist), IMG_SHAPE, IMG_SHAPE))
    for eachimg in path:
        img = cv.imread(os.path.join("%s/%s" % (filepath,eachimg)))
        print(eachimg)
        img = local_threshold(img)
        imgarray[cnt] = np.array(img)
        cnt = cnt + 1
    return imgarray

# lable :
#   0-9 -> 0-9
#   +-*/= -> 10-14
def gettest_lable():
    labelarray = np.zeros((len(samplelist) * TestS))
    cnt = 0
    for i in reversed(range(10)):
        for j in range(TestS):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray


def gettrain_char():
    filepath = "C:/Users/JarvisZhang/Desktop/tmp/Numerals/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((len(samplelist) * Samplesize, IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        child = os.path.join("%s%s" % (filepath, eachpath))
        for filename in os.listdir(child):
            img = cv.imread(os.path.join("%s%s/%s" % (filepath, eachpath, filename)))
            img = local_threshold(img)
            imgarray[cnt] = np.array(img)
            cnt = cnt + 1
            print("%s%s/%s"% (filepath, eachpath, filename))
    return imgarray

# lable :
#   0-9 -> 0-9
#   +-*/= -> 10-14
def gettrain_lable():
    labelarray = np.zeros((len(samplelist) * Samplesize))
    cnt = 0
    for i in range(10):
        for j in range(Samplesize):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray


if __name__ == "__main__":

    # normal char part
    testnormalchar = gettest_char()
    testnormallable = gettest_lable()

    trainnomalchar = gettrain_char()
    trainnomallable = gettrain_lable()


    np.savez("../USPS.npz", traindata= trainnomalchar
             , trainlabel=trainnomallable
             , testdata=testnormalchar
             , testlabel=testnormallable)