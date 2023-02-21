import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)
kerne2 = np.ones((3, 3), np.uint8)

img = cv2.imread('test.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#cvtColor(要轉換的圖片,轉換方式)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #灰階圖
#GaussianBlur(要模糊的圖片, 核, 標準差) 做高斯模糊 
blur = cv2.GaussianBlur(img, (7, 7), 5)
#取得圖片邊緣 差別越大數字越高 小於150不當邊緣 大於200皆當邊緣來看
Canny = cv2.Canny(img, 150, 200)
#dilate(要膨脹的圖, 核(二維陣列), 要膨脹幾次(線條越粗)) 做膨脹效果
dilate = cv2.dilate(Canny, kernel, iterations=1)
#erode(要侵蝕的圖, 核(二維陣列), 要膨脹幾次(線條越細)) 做侵蝕
erode = cv2.erode(dilate, kerne2, iterations=1)

#cv2.imshow('img', img)
#cv2.imshow('gray', gray)
#cv2.imshow('blur', blur)
#cv2.imshow('Canny', Canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)