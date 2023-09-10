import cv2
import numpy as np
def empty(a):
    pass
cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars', 640,240)
cv2.createTrackbar('hue min', 'trackbars', 66, 179,empty)
cv2.createTrackbar('hue max', 'trackbars', 164, 179,empty)
cv2.createTrackbar('sat min', 'trackbars', 84, 255,empty)
cv2.createTrackbar('sat max', 'trackbars', 255, 255,empty)
cv2.createTrackbar('val min', 'trackbars', 0, 255,empty)
cv2.createTrackbar('val max', 'trackbars', 255, 255,empty)

while True:
    img= cv2.imread('/home/sanchali/Downloads/flo.jpeg')
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos('hue min', 'trackbars')
    hmax = cv2.getTrackbarPos('hue max', 'trackbars')
    smin = cv2.getTrackbarPos('sat min', 'trackbars')
    smax = cv2.getTrackbarPos('sat max', 'trackbars')
    vmin = cv2.getTrackbarPos('val min', 'trackbars')
    vmax = cv2.getTrackbarPos('val max', 'trackbars')
    print(hmin,hmax,smin,smax,vmin,vmax)
    lower= np.array([hmin,smin,vmin])
    upper=np.array([hmax,smax,vmax])
    mask = cv2.inRange(imgHSV, lower,upper)
    imgresult=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('original', img)
    cv2.imshow('hsv', imgHSV)
    cv2.imshow('mask', mask)
    cv2.imshow('result', imgresult)
    cv2.waitKey(1)
