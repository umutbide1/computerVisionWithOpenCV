import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("Lenna", img)

#Horizontal yani yan yana birleştirme 
hor = np.hstack((img,img))
cv2.imshow("Merged Image", hor)

# dikey (vertical) birlestirme

ver= np.vstack((img,img))
cv2.imshow("Vertical Merged Images", ver)

