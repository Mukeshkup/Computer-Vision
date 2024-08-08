#To capture the video through web cam

import cv2

''' 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 to access through webcam
print("check===",cap.isOpened())                         #1 for external camera

while(cap.isOpened()):   #It will give true value till it caputes video
    ret, frame = cap.read()   #here read the frame
    
    if ret==True: #if pic is stored in frame it will give true value
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #here flip is used to lip the video at recording time
        #frame = cv2.flip(frame,0)
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
        
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
'''

#To capture the video through web cam and save it
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
print("check===",cap.isOpened())


#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("D:/Computer Vision/Learnings/output.avi",fourcc,20.0,(640,480),0)#If you want gray video ten at last put "0", and if color then nothing is written

while(cap.isOpened()):   
    ret, frame = cap.read()   
    
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        output.write(gray) #if u want color one then write frame in the bracket
        
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
        
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()