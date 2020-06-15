import numpy as np
import cv2
img = cv2.imread('deepika.jpeg')
#print(img.shape)
def click_events(events,x,y,flay,param):
    if events == cv2.EVENT_RBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) +',' +str(y)
        cv2.putText(img,text,(x,y),font,.5,(0,255,255),1)
        cv2.imshow('image',img)
    if events == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        stre = str(blue) + ',' + str(green) + ',' +str(red)
        cv2.putText(img, stre, (x, y), font, .5, (255, 0, 255), 1)
        cv2.imshow('image', img)
    if events == cv2.EVENT_LBUTTONDBLCLK:
        face_cascade = cv2.CascadeClassifier('haarscade.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.imshow('image', img)
    if events == cv2.EVENT_MBUTTONDBLCLK:
        face_cascade = cv2.CascadeClassifier('haarscade.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x1, y1, w, h) in faces:
            new_image = img[y1:h+y1,x1:w+x1]
            cv2.imshow('face',new_image)
            cv2.imshow('image',img)
    if events == cv2.EVENT_MOUSEWHEEL:
        smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        smile = smile_cascade.detectMultiScale(gray, 1.8, 20)
        for (x, y, w, h) in smile:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.imshow('image', img)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
