import random
import os
from PIL import Image, ImageDraw, ImageFont
import shutil
import numpy as np

#
# im_50_blank = Image.new('RGBA', (28, 28), (255, 255, 255,255))
# draw = ImageDraw.Draw(im_50_blank)
#
# font = ImageFont.truetype('arial.ttf', 29)
# num = chr(61)
#
# w1,h1 = font.getsize(num)
# w2,h2 = font.getoffset(num)
# w,h = w1+w2, h1+h2
# print(w,h)
# draw.text(xy=((28 - w) / 2, 0), font=font, text=num, fill=(0, 0, 0, 255))
# im_50_blank.save("C:/Users/JarvisZhang/Desktop/test1.png")

data_path = os.path.abspath(os.path.dirname(__file__)) + '/../normalcal.npz'
data = np.load(data_path)

trainlable = data["trainlabel"];
print((trainlable[6001]))


