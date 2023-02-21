import cv2

img = cv2.imread("shape.jpg")
imgContour = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 130,200) #檢測邊緣

#檢測輪廓
#findContours(要檢測的圖, 內輪廓外輪廓?, 近似方法此處不壓縮選none)
#回傳兩個值(要找的輪廓, 階層)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    print(cnt)
    #畫輪廓,drawContours(要畫在哪張圖,要化的輪廓ㄝ, 要畫得輪廓是第幾個-1代表全部, 輪廓顏色, 線條粗度)
    cv2.drawContours(imgContour, cnt, -1,(255, 0, 0), 4 )

    #cv2.contourArea(cnt) #取每個輪廓的面積
    area = cv2.contourArea(cnt)
    if area > 500:
    #cv2.arcLength(cnt, True)#每個輪廓的邊長 arcLength(輪廓, 是否是閉合的)
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True )#(輪廓, 近似值)
        #print(vertices) 每個多邊形的頂點
        corner = len(vertices)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 4)
        if corner == 3:
            #putText(輪廓?,文字,文字位置,字體,文字大小, 字體顏色,粗度)
            cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
        elif corner == 4:
            cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
        elif corner == 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
        elif corner >= 6:
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)    
#cv2.imshow('img', img)
#cv2.imshow('canny', canny)
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)
