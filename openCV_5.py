#過濾顏色?
import cv2
import numpy as np

def empty(v):
    pass


img = cv2.imread('test.jpg')

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#想要偵測顏色的話將一開始BGR轉換成HSV的圖片，因為HSV在色彩分辨比較好
#H代表色彩，S代表深浅，V代表明暗


cv2.namedWindow('TrackBar') #新視窗
cv2.resizeWindow('TrackBar', 640,320)   #設定新視窗大小

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)#新增控制條元件(名字,在哪個視窗下,控制條初始值,控制條最大值h:0-179, 當控制條被改變後要呼叫的funtion)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #RGB-> H色調S飽和度V亮度
while True:
   h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar') #取得控制條的值
   h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
   s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
   s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
   v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
   v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')

   lower = np.array([h_min, s_min, v_min])
   upper = np.array([h_max, s_max, v_max])
   mask = cv2.inRange(hsv, lower, upper)    #過濾(圖片, 最小值, 最大值)
   result = cv2.bitwise_and(img, img, mask=mask)
   
   cv2.imshow('img', img)
   cv2.imshow('hsv', hsv)
   cv2.imshow('mask', mask)
   cv2.imshow('result', result)
   cv2.waitKey(1)




cv2.waitKey(0)