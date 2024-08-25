"""15"""
#How to create a border for an image using opencv
#with the help of cv2.copyMakeBorder() function.
#it take parameters like(img,border_width*4,bordertype,val_brder)
#border width = top border width,bottom border width,right border width,left border width

import cv2
import numpy as np


img1 = cv2.imread("Data\\lion.jpg")
img1 = cv2.resize(img1,(1000,600))
#creating image border 
brdr = cv2.copyMakeBorder(img1,10,10,5,5,cv2.BORDER_CONSTANT,value = [255,0,125])

cv2.imshow("res",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()