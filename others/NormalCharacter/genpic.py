import random
import os
from PIL import Image, ImageDraw, ImageFont
import shutil

random.seed(3)
path_img = "C:/Users/JarvisZhang/Desktop/now/tmp/Normal/"

def mkdir_for_imgs():
    for i in range(15):
        if os.path.isdir(path_img + "Sample" + "%03d" % i):
            shutil.rmtree(path_img + "Sample" + "%03d" % i, ignore_errors=True)
            print(path_img + "Sample" + "%03d" % i)
            os.mkdir(path_img + "Sample" + "%03d" % i)
        else:
            print(path_img + "Sample" + "%03d" % i)
            os.mkdir(path_img + "Sample" + "%03d" % i)

switch = {
    0:  20,
    1:  21,
    2:  22,
    3:  23,
    4:  24,
    5:  25,
    6:  26,
    7:  27,
    8:  28,
    9:  19
}

outsize = 28

# 生成单张图像
def generate_single(m,index):
    # 先绘制一个50*50的空图像
    im_50_blank = Image.new('RGBA', (outsize, outsize), (255, 255, 255, 255))
    # 创建画笔
    draw = ImageDraw.Draw(im_50_blank)

    if index <= 9:
        num = chr(48+index)
    elif index == 10:
        num = chr(43)
    elif index == 11:
        num = chr(45)
    elif index == 12:
        num = '×'
    elif index == 13:
        num = '÷'
    elif index == 14:
        num = chr(61)


    # if int(m/1000) == 0:
    #     font = ImageFont.truetype('AGENCYR.TTF', switch[m%10])
    # elif int(m/1000) == 1:
    #     font = ImageFont.truetype('arial.ttf', switch[m%10])
    # elif int(m/1000) == 2:
    #     font = ImageFont.truetype('ARLRDBD.TTF', switch[m%10])
    # elif int(m/1000) == 3:
    #     font = ImageFont.truetype('bahnschrift.ttf', switch[m%10])
    # elif int(m/1000) == 4:
    #     font = ImageFont.truetype('BASKVILL.TTF', switch[m%10])
    # elif int(m/1000) == 5:
    #     font = ImageFont.truetype('BRLNSR.TTF', switch[m%10])
    # elif int(m / 1000) == 6:
    #     font = ImageFont.truetype('BOD_R.TTF', switch[m % 10])
    # elif int(m / 1000) == 7:
    #     font = ImageFont.truetype('BKANT.TTF', switch[m % 10])
    # elif int(m / 1000) == 8:
    #     font = ImageFont.truetype('BOOKOSB.TTF', switch[m % 10])
    # elif int(m / 1000) == 9:
    #     font = ImageFont.truetype('calibri.ttf', switch[m % 10])
    # elif int(m / 1000) == 10:
    #     font = ImageFont.truetype('CALIFR.TTF', switch[m % 10])
    # elif int(m / 1000) == 11:
    #     font = ImageFont.truetype('CALIST.TTF', switch[m % 10])
    # elif int(m / 1000) == 12:
    #     font = ImageFont.truetype('cambria.ttc', switch[m % 10])
    # elif int(m / 1000) == 13:
    #     font = ImageFont.truetype('consola.ttf', switch[m % 10])
    # elif int(m / 1000) == 14:
    #     font = ImageFont.truetype('consolab.ttf', switch[m % 10])
    # elif int(m / 1000) == 15:
    #     font = ImageFont.truetype('tahoma.ttf', switch[m % 10])
    # elif int(m / 1000) == 16:
    #     font = ImageFont.truetype('tahomabd.ttf', switch[m % 10])
    # elif int(m / 1000) == 17:
    #     font = ImageFont.truetype('times.ttf', switch[m % 10])
    # elif int(m / 1000) == 18:
    #     font = ImageFont.truetype('timesbd.ttf', switch[m % 10])
    # elif int(m / 1000) == 19:
    #     font = ImageFont.truetype('simfang.ttf', switch[m % 10])
    # elif int(m / 1000) == 20:
    #     font = ImageFont.truetype('simhei.ttf', switch[m % 10])
    # elif int(m / 1000) == 21:
    #     font = ImageFont.truetype('simkai.ttf', switch[m % 10])
    # else:
    #     font = ImageFont.truetype('verdana.ttf', switch[m%10])
    if m // 10 == 0:
        font = ImageFont.truetype('arial.ttf', switch[m % 10])
    elif m // 10 == 1:
        font = ImageFont.truetype('consola.ttf', switch[m % 10])
    elif m // 10 == 2:
        font = ImageFont.truetype('timesbd.ttf', switch[m % 10])
    elif m // 10 == 3:
        font = ImageFont.truetype('cambria.ttc', switch[m % 10])
    elif m // 10 == 4:
        font = ImageFont.truetype('tahoma.ttf', switch[m % 10])
    elif m // 10 == 5:
        font = ImageFont.truetype('simhei.ttf', switch[m % 10])
    elif m // 10 == 6:
        font = ImageFont.truetype('calibri.ttf', switch[m % 10])
    else:
        font = ImageFont.truetype('Dengb.ttf', switch[m % 10])


    w1,h1 = font.getsize(num)
    w2,h2 = font.getoffset(num)
    w,h = w1+w2, h1+h2
    print(num)
    print(w,h)
    if w > outsize:
        x = 0
    else:
        x = (outsize-w)/2
    if h > outsize:
        y = 0
    else:
        y = (outsize-h)/2
    draw.text(xy=(x,y), font=font, text=num, fill=(0, 0, 0, 255))

    return im_50_blank,num


def generate_0toZ(n):
    # 用cnt_num[0]-cnt_num[35]来计0-Z生成的个数，方便之后进行命名
    cnt_num = []
    for i in range(36):
        cnt_num.append(0)

    #n轮
    for m in range(n):
        for index in range(36):
            im,num = generate_single(m,index)
            # 取灰度
            im_gray = im.convert('1')
            cnt_num[index] = cnt_num[index] + 1
            # 输出显示路径
            print("Generate:", path_img + "Sample" + "%03d" % index + "/" + "img%03d" % index + "_" + str(cnt_num[index]) + ".png")
            # 将图像保存在指定文件夹中
            im_gray.save(path_img + "Sample" + "%03d" % index + "/" + "img%03d" % index + "_" + str(cnt_num[index]) + ".png")

    print("\n")
    # 输出分布
    print("生成的0-Z的分布：")
    for k in range(36):
        print("Sample", k if k < 10 else chr(k-10+65), ":", cnt_num[k], "in all")

def generate_symbols(n):
    # 包括符号 + - * / = ()
    # 用cnt_num[0]-cnt_num[35]来计0-Z生成的个数，方便之后进行命名
    cnt_num = []
    for i in range(7):
        cnt_num.append(0)

    # n轮
    for m in range(n):
        for index in range(7):
            im, num = generate_single(m, index)
            # 取灰度
            im_gray = im.convert('1')
            cnt_num[index] = cnt_num[index] + 1
            # 输出显示路径
            print("Generate:",
                  path_img + "Sample" + "%03d" % (index+10) + "/" + "img%03d" % (index+10) + "_" + str(cnt_num[index]) + ".png")
            # 将图像保存在指定文件夹中
            im_gray.save(
                path_img + "Sample" + "%03d" % (index+10) + "/" + "img%03d" % (index+10) + "_" + str(cnt_num[index]) + ".png")

def generate_0tosymbols(n):
    cnt_num = []
    for i in range(15):
        cnt_num.append(0)

    # n轮
    for m in range(n):
        for index in range(15):
            im, num = generate_single(m, index)
            # 取灰度
            im_gray = im.convert('1')
            cnt_num[index] = cnt_num[index] + 1
            # 输出显示路径
            print("Generate:",
                  path_img + "Sample" + "%03d" % (index) + "/" + "img%03d" % (index) + "_" + str(
                      cnt_num[index]) + ".png")
            # 将图像保存在指定文件夹中
            im_gray.save(
                path_img + "Sample" + "%03d" % (index) + "/" + "img%03d" % (index) + "_" + str(
                    cnt_num[index]) + ".png")


if __name__ == "__main__":
    mkdir_for_imgs()
   # generate_0toZ(1)
   # generate_symbols(50)
    generate_0tosymbols(1400)
   # generate_single(20,14)
