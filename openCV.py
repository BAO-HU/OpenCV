# import cv2

# img = cv2.imread ('aa.png')

# img = cv2.resize(img, (0, 0), fx= 0.5, fy= 0.5) 
# #img = cv2.resize(img,(300,300)) 300x300
# #img = cv2.resize(img, (0, 0), fx= 0.5, fy= 0.5) fx fy倍數
 

# cv2.imshow('img',img)
# cv2.waitKey(0)

#------讀取影片------#
#影片為很多張圖片
import cv2
cap = cv2.VideoCapture('test.mp4') #cap = cv2.VideoCapture(0) 代表取得視訊鏡頭


while True:
    
    ret, frame = cap.read() #回傳兩個值(ret取得下一張圖片有無取得成功(bool),frame取得影片下一張圖片(圖片))
    
    if ret:
        frame = cv2.resize(frame, (0,0), fx=0.6, fy=0.6)
        #frame = cv2.resize(frame,(2000,100))
        cv2.imshow('video', frame)
        print("AA")
    else:
        break
    if cv2.waitKey(10) == ord('q'): #提早按下q結束
        break
    #cv2.waitKey(1000) #每10毫秒下一幀數