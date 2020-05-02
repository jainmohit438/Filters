
import cv2
import sys


def color_invert(src):
    img_bgr = cv2.split(src)

    dst = cv2.merge((255 - img_bgr[0] , 255 - img_bgr[1], 255 - img_bgr[2]))

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


    output_img = color_invert(input_img)

    cv2.imwrite("invert_" + param[1], output_img)
