import cv2
import datetime
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('2 video.avi', fourcc,20.0,(640,480))
print(cap.isOpened())
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
       # out.write(frame)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #text = 'width' + str(cap.get(3)) + 'Height' +str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame  = cv2.putText(frame,datet,(10,50),font,2,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('video', frame)

        k = cv2.waitKey(0)
        if k == ord('s'):
            break
    else:
        break
cap.release()
#out.release()
cv2.destroyAllWindows()