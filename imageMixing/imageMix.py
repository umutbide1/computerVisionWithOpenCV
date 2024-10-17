import cv2 
import numpy as np
import pandas as pd 
import matplotlib as plt

img1= cv2.imread("img1.JPG")
img2= cv2.imread("img2.JPG")
img3= cv2.imread("img3.jpg")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)