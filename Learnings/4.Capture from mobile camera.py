#How to use android device camera as webcam in OPencv.

import cv2

camera="http://192.168.1.2:8080/video"

#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0)
cap.open(camera)
print("check===",cap.isOpened())

'''
If want to save 

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
'''
while(cap.isOpened()):
    ret, frame = cap.read()   
    if ret == True:
    
        frame = cv2.resize(frame,(700,700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #output.write(frame)   if want to save
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   
            break
    
cap.release()
#output.release()
cv2.destroyAllWindows()
