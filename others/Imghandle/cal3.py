import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2 as cv
import numpy as np
import random

np.set_printoptions(threshold=np.inf)
IMG_SHAPE = 28

Samplesize = 6000
TestS = 1000

samplelist = []



def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 2.5)
    cv.bitwise_not(binary,binary)
    return binary


def gettest_normalchar():
    filepath = "C:/Users/JarvisZhang/Desktop/new/"
    path = os.listdir(filepath)
    cnt = 0
    imgarray = np.zeros((TestS*len(samplelist), IMG_SHAPE, IMG_SHAPE))
    for eachpath in path:
        # choose
        if eachpath  not in samplelist:
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
    filepath = "C:/Users/JarvisZhang/Desktop/new/"
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

# def gettest_hndchar():
#     filepath = "C:/Users/JarvisZhang/Desktop/new/"
#     path = os.listdir(filepath)
#     cnt = 0
#     imgarray = np.zeros((TestS * len(samplelist_s), IMG_SHAPE, IMG_SHAPE))
#     for eachpath in path:
#         # choose
#         if eachpath not in samplelist_s:
#             continue
#         child = os.path.join("%s%s" % (filepath, eachpath))
#         childpath = os.listdir(child)
#         for index in range(TestS):
#             while True:
#                 num = random.randint(0, Samplesize - 1)
#                 if childpath[num] not in testhndname:
#                     testhndname.append(childpath[num])
#                     break
#             img = cv.imread(os.path.join("%s%s/%s" % (filepath, eachpath, childpath[num])))
#             img = local_threshold(img)
#             imgarray[cnt] = np.array(img)
#             cnt = cnt + 1
#             print(childpath[num])
#     return imgarray
# # lable :
# #   0-9 -> 0-9
# #   +-*/= -> 10-14
# def gettest_hndlable():
#     labelarray = np.zeros((len(samplelist_s) * TestS))
#     cnt = 0
#     for i in range(10,15):
#         for j in range(TestS):
#             labelarray[cnt] = i
#             cnt = cnt + 1
#     return labelarray
#
# def gettrain_hndchar():
#     filepath = "C:/Users/JarvisZhang/Desktop/calculator2/"
#     path = os.listdir(filepath)
#     cnt = 0
#     imgarray = np.zeros((len(samplelist_s) * Samplesize, IMG_SHAPE, IMG_SHAPE))
#     for eachpath in path:
#         # choose
#         if eachpath not in samplelist_s:
#             continue
#         child = os.path.join("%s%s" % (filepath, eachpath))
#         for filename in os.listdir(child):
#             if filename in testhndname:
#                 continue
#             img = cv.imread(os.path.join("%s%s/%s" % (filepath, eachpath, filename)))
#             img = local_threshold(img)
#             imgarray[cnt] = np.array(img)
#             cnt = cnt + 1
#             print(filename)
#     return imgarray
# # lable :
# #   0-9 -> 0-9
# #  +-*/= -> 10-14
# def gettrain_hndlable():
#     labelarray = np.zeros((len(samplelist_s) * Samplesize))
#     cnt = 0
#     for i in range(10,15):
#         for j in range(Samplesize):
#             labelarray[cnt] = i
#             cnt = cnt + 1
#     return labelarray








if __name__ == "__main__":
    # data_path = os.path.abspath(os.path.dirname(__file__)) + '/../cal3.npz'
    # data = np.load(data_path)
    # print(data['traindata'].shape)

    # normal char part
    testnormalname = []
    testnormalchar = gettest_normalchar()
    testnormallable = gettest_normallable()

    trainnomalchar = gettrain_normalchar()
    trainnomallable = gettrain_normallable()

    # # Hnd char part
    # testhndname = []
    # testhndchar = gettest_hndchar()
    # testhndlable = gettest_hndlable()
    #
    # trainhndchar = gettrain_hndchar()
    # trainhndlable = gettrain_hndlable()
    #
    # print(trainnomalchar.shape)
    # print(trainhndchar.shape)
    #
    #
    # data_path = os.path.abspath(os.path.dirname(__file__)) + '/../mnist.npz'
    # data = np.load(data_path)
    # trainhndchar = np.append(trainhndchar, data['x_train'])
    # testhndchar = np.append(testhndchar , data['x_test'])
    # trainhndlable = np.append(trainhndlable , data['y_train'])
    # testhndlable = np.append(testhndlable , data['y_test'])
    #
    # print(trainhndchar.shape)

    # np.savez("../cal3.npz", traindata=np.append(trainnomalchar, trainhndchar)
    #          , trainlabel=np.append(trainnomallable, trainhndlable)
    #          , testdata=np.append(testnormalchar, testhndchar)
    #          , testlabel=np.append(testnormallable, testhndlable))

    np.savez("../normalcal.npz", traindata= trainnomalchar
             , trainlabel=trainnomallable
             , testdata=testnormalchar
             , testlabel=testnormallable)