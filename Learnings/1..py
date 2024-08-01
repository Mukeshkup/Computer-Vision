# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:45:31 2024

@author: mukes
"""

import cv2     #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location

img=cv2.imread("D:\Computer Vision\Learnings\captain.jpeg",1)  #"1" is for colored image
img= cv2.resize(img,(500,750))  
cv2.imshow("Colored Image",img)  #It accept two parameters 1)- Name of screen , 2) - Image
print("Give image with color==\n",img)
cv2.waitKey(1110)            # here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()


#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
img1=cv2.imread("D:\Computer Vision\Learnings\captain.jpeg",0) #"0" is for gray scaled imag
img1=cv2.resize(img1, (500,750))
cv2.imshow("Gray Scale Image",img1)
print("Image in gray scale==\n",img1)
cv2.waitKey(300)           
cv2.destroyAllWindows()


#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel(Saturates the image)
img3 = cv2.imread("D:\Computer Vision\Learnings\captain.jpeg",-1)#"-1" increases the saturation f the image
img3 = cv2.resize(img3,(580,700))#width ,height
cv2.imshow("Original Image",img3)
print("Image in original value==\n",img3)
cv2.waitKey(1110)           
cv2.destroyAllWindows()


#Flip the image
img4=cv2.imread("D:\Computer Vision\Learnings\captain.jpeg")
img4=cv2.flip(img4,0) #it accept 3 parameters 0,-1,1    1-mirror flip
cv2.imshow("Fliped Image",img4)                   #     0-top-bottom flip      
cv2.waitKey(3310)                                 #    -1 - mirror + top bottom flip
cv2.destroyAllWindows()