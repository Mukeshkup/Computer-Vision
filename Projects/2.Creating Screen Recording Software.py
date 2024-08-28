import cv2 as c
import pyautogui as p
import numpy as np

#Create resolution
rs = p.size() #It captures screen's resolution

#filename in which we store recording
fn = input("Please Enter any file name and Path")

#Fix the frame rate
fps = 30.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create recording module
c.namedWindow("LIve_Recording",c.WINDOW_NORMAL) #Name of the window

#Resize the window
c.resizeWindow("Live",(600,400))

while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = c.cvtColor(f,c.COLOR_BGR2RGB) #Opencv reads color in BGR, we have to convert it in RGB
    output.write(f)    #Save the photos
    c.imshow("screenshot", f)
    if c.waitKey(1) == ord("q"):
        break

c.destroyAllWindows()
output.release()  
    