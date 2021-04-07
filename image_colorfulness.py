#Hasler and Süsstrunk formula
#R-G  以及 0.5*(R+G) - B 之后绝对值的标准差与均值的计算
#coding=utf8


import numpy as np
import cv2

def hasler_formla_colorfulness(image_color):
    '''
        图片色彩丰富度
        return value range: 0~100
    '''
    (B, G, R) = cv2.split(image.astype("float"))

    R_minus_G = np.absolute(R - G)
    RG_minus_B = np.absolute(0.5 * (R + G) - B)

    return 0.3 * (np.sqrt(np.mean(R_minus_G) ** 2 + np.mean(RG_minus_B))) + (np.sqrt( np.std(R_minu_G) ** 2 + np.std(RG_minus_B) ** 2))


