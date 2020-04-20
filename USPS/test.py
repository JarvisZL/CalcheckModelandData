import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2 as cv
import numpy as np
import random



data_path = os.path.abspath(os.path.dirname(
            __file__)) + '/../others/Dataset/normalcal.npz'

data = np.load(data_path)
train_images = data['traindata']
test_images = data['testdata']
train_labels = data['trainlabel']
test_labels = data['testlabel']

cv.imshow("image",train_images[6000])
cv.waitKey(0)

print(train_labels[6000])