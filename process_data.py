import cv2
import numpy as np

#读取文本文件，并将每个字符编码为int格式
def load_txt(path):
    with open(path) as f:
        lines = f.readlines()

    lines = [[ord(c) for c in line] for line in lines]

    return lines

#将int格式的字符编码转化为文本
def to_str(notation):
    string_to_display = ""
    for l in notation:
        for c in l:
            string_to_display += chr(c)
    return string_to_display

#读取图片，并获取灰度图像中各个位置的像素值
def load_img(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).tolist()
    return img

#将存储为数值矩阵的图像可视化
def display_img(matrix, name):
    img = np.array(matrix).astype(np.uint8)
    cv2.imwrite('./img/' + name + '.png',img)
    