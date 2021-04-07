import numpy as np
import cv2

def get_var_pics(image_gray):
    #图像清晰度，划分9X9，判断其中低清晰度占比防止背景虚化、部分纯色导致的误判
    image_gray_raw = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    height, width = image_gray.shape

    varList = []
    m = 9
    n = 9
    height_unit = height // m
    width_unit = width // n
    
    for i in range(m):
        for j in range(n):
            target_region = image_gray[height_unit*i:height_unit*(i+1), width_unit*j:width_unit*(j+1)]
            imageVar = cv2.Laplacian(target_region, cv2.CV_64F).var()
            varList.append(imageVar)
    varArray = np.array(varList)
    avg_var, std_var = np.average(varList), np.std(varList) 

    return avg_var, std_var

def get_cartoon_index(img_color):
    #是否为卡通图，indx值越低，特别是avg_indx, avg_var都很低时，最有有可能是卡通图
    cartoon_index = cv2.mean(img_color - cv2.medianBlur(img_color, 5))
    avg_indx = np.average(cartoon_index[0:3])
    std_indx = np.std(cartoon_index[0:3])
    
    return avg_indx, std_indx
