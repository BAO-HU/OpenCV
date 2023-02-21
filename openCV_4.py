import cv2
import numpy as np

img = np.zeros((600,600,3), np.uint8)

###line(要畫線的那張圖,線的第一點,線的第二點,顏色,粗度) 畫線
#cv2.line(img, (0,0), (400,300), (0,255,0), 2 )
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 2 ) 

#rectangle(要畫線的那張圖,方形左上的第一點,方形右下的第二點,顏色,粗度) 畫方形
cv2.rectangle(img, (0,0), (400, 300), (0,0,255), 2 ) #粗度填入cv2.FILLED為填滿方形

#circle(要畫線的那張圖,中心點,半徑,顏色,粗度) 畫圓形
cv2.circle(img, (300,400), 30, (255,0,0), cv2.FILLED)

###putText(要畫線的那張圖,要寫的文字, 座標(文字左下角的位子),字體,文字大小,文字顏色,文字粗細)
#不支援中文
cv2.putText(img, 'Hello', (100,500), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)