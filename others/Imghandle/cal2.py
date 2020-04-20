import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2 as cv
import numpy as np
import random

np.set_printoptions(threshold=np.inf)
IMG_SHAPE = 28
Samplesize1 = 1000
TestS1 = 50
samplelist1 = ["Sample000","Sample001","Sample002","Sample003","Sample004","Sample005","Sample006","Sample007","Sample008",
              "Sample009","Sample010","Sample011","Sample012","Sample013","Sample014"]
Samplesize2 = 1000
TestS2 = 45
samplelist2 =["Sample015","Sample016","Sample017","Sample018","Sample019","Sample020","Sample021","Sample022","Sample023",
              "Sample024","Sample025","Sample026","Sample027","Sample028","Sample029"]

def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 2.5)
    cv.bitwise_not(binary,binary)
    return binary


def gettest_normalchar():
    filepath = "C:/Users/JarvisZhang/Desktop/calculator2/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((TestS1*len(samplelist1), IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath  not in samplelist1:
            continue
        child = os.path.join("%s%s" % (filepath, eachpath))
        childpath = os.listdir(child)
        for index in range(TestS1):
            while True:
                num = random.randint(0,Samplesize1-1)
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
    labelarray = np.zeros((len(samplelist1) * TestS1))
    cnt = 0
    for i in range(15):
        for j in range(TestS1):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray

def gettrain_normalchar():
    filepath = "C:/Users/JarvisZhang/Desktop/calculator2/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((len(samplelist1) * Samplesize1, IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath not in samplelist1:
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
    labelarray = np.zeros((len(samplelist1) * Samplesize1))
    cnt = 0
    for i in range(15):
        for j in range(Samplesize1):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray

def gettest_hndchar():
    filepath = "C:/Users/JarvisZhang/Desktop/calculator2/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((TestS2 * len(samplelist2), IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath not in samplelist2:
            continue
        child = os.path.join("%s%s" % (filepath, eachpath))
        childpath = os.listdir(child)
        for index in range(TestS2):
            while True:
                num = random.randint(0, Samplesize2 - 1)
                if childpath[num] not in testhndname:
                    testhndname.append(childpath[num])
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
def gettest_hndlable():
    labelarray = np.zeros((len(samplelist2) * TestS2))
    cnt = 0
    for i in range(15):
        for j in range(TestS2):
            labelarray[cnt] = i
            cnt = cnt + 1
    return labelarray

def gettrain_hndchar():
    filepath = "C:/Users/JarvisZhang/Desktop/calculator2/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((len(samplelist2) * Samplesize2, IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath not in samplelist2:
            continue
        child = os.path.join("%s%s" % (filepath, eachpath))
        for filename in os.listdir(child):
            if filename in testhndname:
                continue
            img = cv.imread(os.path.join("%s%s/%s" % (filepath, eachpath, filename)))
            img = local_threshold(img)
            imgarray[cnt] = np.array(img)
            cnt = cnt + 1
            print(filename)
    return imgarray
# lable :
#   0-9 -> 0-9
#  +-*/= -> 10-14
def gettrain_hndlable():
    labelarray = np.zeros((len(samplelist2) * Samplesize2))
    cnt = 0
    for i in range(15):
        for j in range(Samplesize2):
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

    #Hnd char part
    testhndname = []
    testhndchar = gettest_hndchar()
    testhndlable = gettest_hndlable()

    trainhndchar = gettrain_hndchar()
    trainhndlable = gettrain_hndlable()

    np.savez("../cal2.npz", traindata=np.append(trainnomalchar, trainhndchar)
             , trainlabel=np.append(trainnomallable, trainhndlable)
             , testdata=np.append(testnormalchar, testhndchar)
             , testlabel=np.append(testnormallable, testhndlable))