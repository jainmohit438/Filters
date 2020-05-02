# -*- coding: utf-8 -*-
import cv2
import sys

# extract color function
def color_gray(src):
    img_bgr = cv2.split(src)
    dst = cv2.merge(((img_bgr[0] + img_bgr[1] + img_bgr[2])/3, (img_bgr[0] + img_bgr[1] + img_bgr[2])/3, (img_bgr[0] + img_bgr[1] + img_bgr[2])/3))

    return dst

if __name__ == '__main__':
    param = sys.argv
    
    try:
        input_img = cv2.imread(param[1])
    except:
        print ('faild to load %s' % param[1])
        quit()

    if input_img is None:
        print ('faild to load %s' % param[1])
        quit()

    # making mask using by extract color function
    output_img = color_gray(input_img)

    cv2.imwrite("gray_" + param[1], output_img)
