import cv2 
import matplotlib.pyplot as plt

img1= cv2.imread("img1.JPG")
img2= cv2.imread("img2.JPG")
img3= cv2.imread("img3.jpg")

# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("img3", img3)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

