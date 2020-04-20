import os
import cv2 as cv
import numpy as np
import threading
np.set_printoptions(threshold=np.inf)

IMG_SHAPE = 28

def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 25, 2.5)
    return binary

def Recify(Img):
    tmp = local_threshold(Img)
    h,w = Img.shape[0:2]
    print(h,w)
    bottom = right = 0
    top = left = 2000
    for x in range(h):#[0,899]
        for y in range(w):#[0,1199]
            if tmp[x][y] == 0:
                top = x if x < top else top
                bottom = x if x > bottom else bottom
                left = y if y < left else left
                right = y if y > right else right
    #border
  #  print("first",top,bottom,left,right)
  #   border1  = int((maxm - (bottom-top))/2)
  #   top = top - border1 if top - border1 >= 0 else top
  #   bottom = bottom + border1 if bottom + border1 < h else bottom
  #   border2 = int((maxm - (right-left))/2)
  #   left = left - border2 if left- border2 >= 0 else left
  #   right = right + border2 if right + border2 < w else right
  #  print("second",top, bottom, left, right)

    height = bottom - top
    width = right - left
    maxm = int(2*max(height, width))

    ret = Img[top:bottom, left:right]
    ret = cv.copyMakeBorder(ret,int((maxm - height)/2), int((maxm - height)/2), int((maxm - width)/2), int((maxm - width)/2), cv.BORDER_CONSTANT, value=[255,255,255])

    return ret



def ResizeImg(filepath):
    path = os.listdir(filepath)
    for filename in path:
        img = cv.imread(os.path.join("%s/%s" %(filepath,filename)))
        img = Recify(img)
        nimg = cv.resize(img,(IMG_SHAPE,IMG_SHAPE), interpolation = cv.INTER_AREA)
        cv.imwrite(os.path.join("%s/%s" %(filepath,filename)),nimg)
        print(filename)

def ResizeImgsingle(p):
    filepath = "C:/Users/JarvisZhang/Desktop/now/tmp/Normal/"+p
    path = os.listdir(filepath)
    for eachimg in path:
        img = cv.imread(os.path.join("%s/%s" % (filepath, eachimg)))
        img = Recify(img)
        nimg = cv.resize(img, (IMG_SHAPE, IMG_SHAPE), interpolation=cv.INTER_AREA)
        cv.imwrite(os.path.join("%s/%s" % (filepath, eachimg)), nimg)
        print(eachimg)

if __name__ == '__main__':

    #ResizeImg("C:/Users/JarvisZhang/Desktop/tmp/Test")

     t1 = threading.Thread(target=ResizeImgsingle, args=("Sample014",))
     t2 = threading.Thread(target=ResizeImgsingle, args=("Sample013",))
     t3 = threading.Thread(target=ResizeImgsingle, args=("Sample012",))
     t4 = threading.Thread(target=ResizeImgsingle, args=("Sample011",))
     t5 = threading.Thread(target=ResizeImgsingle, args=("Sample010",))
     t1.start()
     t2.start()
     t3.start()
     t4.start()
     t5.start()


    # ResizeImgsingle("Sample023")

