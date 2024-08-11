"""9"""
import numpy as np
import cv2


img = cv2.imread("Data\\thor.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---


img = np.zeros([512, 512, 3], np.uint8)*255  #zeros For black screen
#img = np.ones([512,512,3], np.uint8)*255 #ones is used to create window of an white screen

"""TO get color codes, go to online color pickler in the broswer and choose the color.
You get color code in RGB format.But while writing in the code change RGB to BGR format
For example if color code is (1,2,3) in RGB, then (3,2,1) in BGR format"""

#Here line accept 5 parameter (img,starting,ending,color,thickness)
img = cv2.line(img, (0,0), (200,200), (154, 92, 424), 8) #color format BGR 

#arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness) 
img = cv2.arrowedLine(img, (0,125), (255,255), (255, 0, 125), 10)

#Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 8)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), -1) #-ve value-it will fill the color in the rectangle

#circle - accept(img,star_co,radius,color,thickness)
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), -5) #As -ve value is there,it will be color filled in the circle

font = cv2.FONT_ITALIC
#puttext -accept(img,text/Title of image,start_co,font,fontsize,color,thickness,linetype)
img = cv2.putText(img, 'THOR', (20, 500), font, 4, (0, 125, 255), 10,cv2.LINE_AA)

#ellipse-accept(img,start_cor,(length,height),2 rotational points,degree,color,thickness)
img = cv2.ellipse(img,(400,600),(100,50),0,0,180,155,5)


pts = np.array([[100,150],[200,30],[170,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,155))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows() 