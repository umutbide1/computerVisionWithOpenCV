import cv2 
import matplotlib.pyplot as plt

img1= cv2.imread("img1.JPG")
img1= cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2= cv2.imread("img2.JPG")
img2= cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3= cv2.imread("img3.jpg")
img3= cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("img3", img3)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

plt.figure()
plt.imshow(img3)