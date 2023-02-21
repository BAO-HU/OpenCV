import cv2
import numpy as np #取微np

import random

img = cv2.imread('test.png')

# print(type(img))#python裡沒有多微陣列 是在numpy裡
# print(img.shape) #陣列大小
#RGB-> BGR

#img = np.empty((300,300,3), np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

newImg = img[:150, :200] #0:150, 0:200

cv2.imshow('img',img)
cv2.imshow('newImg',newImg)
cv2.waitKey(0)

