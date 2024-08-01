#Image conversion project 
#In this project basically we have to convert a Colored picture into a Gray scaled picture.
"""--------------------------------------------------------------------------------------------"""

import cv2

#Taking Input
path_of_image = input(r"Enter the path and name of the image")
print("You Enter this==",path_of_image)

#Now read the image and covert it to grayscale
img = cv2.imread(path_of_image,0)
img = cv2.resize(img,(500,700))
cv2.imshow("converted image==",img)

#if user type s the the pic will be saved
switch = cv2.waitKey(0) & 0xFF
if switch == ord("s"):
    cv2.imwrite("D:\Computer Vision\Projects\output.jpeg",img) #Name of the converted image is output and its saving path
    cv2.destroyAllWindows()                                     ##it accept name of image and data
else:
    cv2.destroyAllWindows()