# beyaz bölgeleri açma ya da kapatma için kullanılır gürültü gidermede fayda sağlıyoruz

# genişleme ve erozyon denen kavramları şimdi işleyeceğiz 

import cv2
import matplotlib.pyplot as plt
import numpy as np
img2 = cv2.imread("35705.jpg")
img = cv2.imread("datai.jpg",0)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Orijinal Goruntu"), plt.show()

# erozyon
kernel = np.ones((5,5),dtype=np.uint8)
result = cv2.erode(img, kernel,iterations=1)

plt.figure(),plt.imshow(result),plt.axis("off"),plt.title("Erozyona ugramıs Goruntu"), plt.show()

# şimdi de genişleteceğiz 

result2 = cv2.dilate(img, kernel,iterations=3)
plt.figure(),plt.imshow(result2),plt.axis("off"),plt.title("Genisletilmis Goruntu"), plt.show()

result3 = cv2.dilate(img2, kernel,iterations=5)
plt.figure(),plt.imshow(result3),plt.axis("off"),plt.title("Ucak deneme kalinlastirilmis Goruntu"), plt.show()

result4 = cv2.erode(img2, kernel,iterations=2)
plt.figure(),plt.imshow(result4),plt.axis("off"),plt.title("Ucak deneme erozyon Goruntu"), plt.show()

# açılma yöntemi beyaz gürültüyü azaltacağız 

whiteNoise = np.random.randint(0,2,size=img.shape[:2]) 
whiteNoise = whiteNoise*255
plt.figure(),plt.imshow(whiteNoise,cmap="gray"),plt.axis("off"),plt.title("White Noise"), plt.show() # burada gürültü oluşturuluyor

noisy_image = whiteNoise + img
plt.figure(),plt.imshow(noisy_image,cmap="gray"),plt.axis("off"),plt.title("Birlesmis Goruntu"), plt.show() # gürültü ve normal resmin karışımı

opening = cv2.morphologyEx(noisy_image.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(),plt.imshow(opening,cmap="gray"),plt.axis("off"),plt.title("Acilmis Goruntu"), plt.show() # gürültü ve normal resmin karışımı

# önce erozyon sonra genişleme yapılarak gürültüden kurtulduk

# black noise

blackNoise = np.random.randint(0,2,size=img.shape[:2]) 
whiteNoise = blackNoise*(-255)
plt.figure(),plt.imshow(blackNoise,cmap="gray"),plt.axis("off"),plt.title("Black Noise"), plt.show()

noisy_image_img = blackNoise + img

plt.figure(),plt.imshow(noisy_image_img,cmap="gray"),plt.axis("off"),plt.title("Black Noise ve img merge"), plt.show()


# kapatma kısmı var ama ihtiyacım olunca döneceğim 
# gradiant kenar tespiti yapıyor o yüzden tekrar bir bakacağız bu konuya yarın 





















