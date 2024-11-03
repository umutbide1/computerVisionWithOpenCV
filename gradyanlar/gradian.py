# görüntüdeki yoğunluk veya renkteki yönlü değişiklik imiş

import cv2
import matplotlib.pyplot as plt 

img = cv2.imread("sudoku.jpg",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("Sudoku resmi"),plt.show()

# x gradyanını bulalım

sobelX = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0)
plt.figure(),plt.imshow(sobelX,cmap="gray"),plt.axis("off"),plt.title("X ekseninde gradyani alinmis sudoku resmi"),plt.show()

# y gradyanını bulalım 

sobelY = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1)
plt.figure(),plt.imshow(sobelY,cmap="gray"),plt.axis("off"),plt.title("Y ekseninde gradyani alinmis sudoku resmi"),plt.show()

# iki tarafında aynı anda gradyanını almak istersem laplacian kullanıyorum

laplacian = cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian,cmap="gray"),plt.axis("off"),plt.title("Laplacian"),plt.show()
