import csv
import os
import logging
import cv2 as cv
import numpy as np
def decode(decode_pixel,defect_type,img_shape,model=True):
    '''
    :param decode_pixel:
    :param defect_type:
    :param img_shape:
    :param model:是否产生二值图像
    :return:mask,status状态码
    '''
    status = 1
    h,_ = img_shape
    mask = np.zeros(img_shape, int)
    decode_pixel = [int(x) for x in decode_pixel.split(" ")]#解析
    initial = decode_pixel[::2]
    increment = decode_pixel[1::2]
    if len(increment) != len(initial):
        status = -1
    else:
        for l in range(len(increment)):
            k = increment[l]
            p = initial[l]
            for i in range(k):
                pt = p + i - 1
                c = pt // h
                r = pt % h
                try:
                    mask[r][c] = int(defect_type) if not model else 255
                except IndexError:
                    status = -2
    return mask,status

def mask(csv_path,img_path,save_path,img_shape = (256,1600)):
    '''
    :param csv_path:
    :param img_path:
    :param img_shape: 默认256*1600
    :return:返回迭代器
    '''
    #mask = np.zeros(img_shape,int)
    with open(csv_path) as label:
        read = csv.reader(label)
        for line in read:
            img_name,defect_type,encodedpixels = line
            image_path = os.path.join(img_path, img_name)#图片路径
            if os.path.exists(image_path):
                mask,status = decode(encodedpixels,defect_type,img_shape)
                if status<= 0:
                    if status == -1:
                        logging.warning("检查"+img_name+"对应的标签文件")
                    elif status == -2:
                        logging.warning("检查"+img_name+"对应的标签文件,解码数组越界")
                yield mask,defect_type,img_name
                # save_dir_path = save_path + "\\defect_type=" + defect_type
                # if not os.path.exists(save_dir_path):
                #     os.makedirs(save_dir_path)
                # cv.imwrite(save_dir_path + "\\" + img_name,mask)
            else:
                logging.warning("文件"+img_name+"不在图片文件夹中")
                continue
