import numpy as np
import cv2
img = cv2.imread('nature.jpg')
def click_events(events,x,y,flay,param):
    if events == cv2.EVENT_RBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) +',' +str(y)
        cv2.putText(img,text,(x,y),font,0.5,(0,255,255),1)
        cv2.imshow('image',img)
    if events == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strings = str(blue) + ',' + str(green) + ',' +str(red)
        cv2.putText(img, strings, (x, y), font, 0.5, (255, 0, 255), 1)
        cv2.imshow('image', img)
#img = np.zeros((512,512,3),np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()

