import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2 as cv
import numpy as np
import random

np.set_printoptions(threshold=np.inf)
IMG_SHAPE = 28

Samplesize = 350
TestS = 10

samplelist = ["Sample00","Sample01","Sample02","Sample03","Sample04","Sample05","Sample06","Sample07","Sample08",
              "Sample09","Sample10","Sample11","Sample12","Sample13","Sample14"]


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 2.5)
    cv.bitwise_not(binary,binary)
    return binary


def gettest_normalchar():
    filepath = "C:/Users/JarvisZhang/Desktop/now/Normal/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((TestS*len(samplelist), IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath not in samplelist:
            continue
        child = os.path.join("%s%s" % (filepath, eachpath))
        childpath = os.listdir(child)
        for index in range(TestS):
            while True:
                num = random.randint(0,Samplesize-1)
                if childpath[num] not in testnormalname:
                    testnormalname.append(childpath[num])
                    break
            img = cv.imread(os.path.join("%s%s/%s" % (filepath, eachpath, childpath[num])))
            img = local_threshold(img)
            imgarray[cnt] = np.array(img)
            cnt = cnt + 1
            print(childpath[num])
    return imgarray

# lable :
#   0-9 -> 0-9
#   +-*/= -> 10-14
def gettest_normallable():
    labelarray = np.zeros((len(samplelist) * TestS))
    cnt = 0
    for i in range(15):
        for j in range(TestS):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray


def gettrain_normalchar():
    filepath = "C:/Users/JarvisZhang/Desktop/now/Normal/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((len(samplelist) * Samplesize, IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath not in samplelist:
            continue
        child = os.path.join("%s%s" % (filepath, eachpath))
        for filename in os.listdir(child):
            if filename in testnormalname:
                continue
            img = cv.imread(os.path.join("%s%s/%s" % (filepath, eachpath, filename)))
            img = local_threshold(img)
            imgarray[cnt] = np.array(img)
            cnt = cnt + 1
            print(filename)
    return imgarray

# lable :
#   0-9 -> 0-9
#   +-*/= -> 10-14
def gettrain_normallable():
    labelarray = np.zeros((len(samplelist) * Samplesize))
    cnt = 0
    for i in range(15):
        for j in range(Samplesize):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray





if __name__ == "__main__":

    # normal char part
    testnormalname = []
    testnormalchar = gettest_normalchar()
    testnormallable = gettest_normallable()

    trainnomalchar = gettrain_normalchar()
    trainnomallable = gettrain_normallable()

    np.savez("../Dataset/normalinandroid.npz", traindata= trainnomalchar
             , trainlabel=trainnomallable
             , testdata=testnormalchar
             , testlabel=testnormallable)