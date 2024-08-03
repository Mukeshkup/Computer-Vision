#How to read Video from any folder using opencv

import cv2

#Here with the help of videoCapture fucntion we easily ready any video.

cap = cv2.VideoCapture("D:\Computer Vision\Learnings\pirate.mp4")  #Here parameter is a path of any video
print("Capture",cap)

#get height and width of frame
print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    ret,frame = cap.read() #As we know video is a collection of pictures so in the frame variable all the pictures are stored     
    frame = cv2.resize(frame,(750,500))                                     # and in the ret variable boolean value is stored
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #To convert in gray
    #frame = cv2.flip(frame, 0) # IF u want to flip
    cv2.imshow("Color Frame", frame)
    cv2.imshow("Gray Frame",gray)
    if cv2.waitKey(25) & 0xFF == ord("q"):  #press to exit
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()    