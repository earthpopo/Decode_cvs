import cv2
import numpy as np
def find_rect(mask):
    rect_list = []
    mask = np.uint8(mask)
    kernal = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)#开运算
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cont in contours:
        x, y, w, h = cv2.boundingRect(cont)
        x1,y1 = x,y
        x2,y2 = x + w, y + h
        rect_list.extend([x1,y1,x2,y2])
        cv2.rectangle(mask, (x1,y1), (x2,y2), (255, 0, 255), 1)
    #cv2.imwrite("test1.jpg",mask)
    return mask,rect_list