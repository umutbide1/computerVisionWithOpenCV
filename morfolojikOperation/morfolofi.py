# beyaz bölgeleri açma ya da kapatma için kullanılır gürültü gidermede fayda sağlıyoruz

# genişleme ve erozyon denen kavramları şimdi işleyeceğiz 

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai.jpg")
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Orijinal Goruntu"), plt.show()

# erozyon
kernel = np.ones((5,5),dtype=np.uint8)
result = cv2.erode(img, kernel,iterations=1)

plt.figure(),plt.imshow(result),plt.axis("off"),plt.title("Oynanmıs Goruntu"), plt.show()
