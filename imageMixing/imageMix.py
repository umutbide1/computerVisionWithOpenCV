import cv2 
import matplotlib.pyplot as plt

# matplotlib de renk skalası RGB şeklindeyken openCV de renk skalası BGR şekilde o yüzden openCV de içeri aldığımız
# fotoğrafta mavi tonlar kırmızı, kırmızı tonlar ise mavi çıkıyor. Bunu önlemek için openCV de
# cv2.cvtColor(img,cv2.COLOUR_BGR2RGB) fonksiyonunu kullanıyoruz.
img1= cv2.imread("img1.JPG") 
img1= cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) 

img2= cv2.imread("img2.JPG")
img2= cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3= cv2.imread("img3.jpg")
img3= cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

# plt.figure()
# plt.imshow(img1)

# plt.figure()
# plt.imshow(img2)

# plt.figure()
# plt.imshow(img3)

print(img1.shape)
print(img2.shape)  # aynı bıyutta mı diye kontrol ediyoruz 
# aynı boyutta değiller (836, 1278, 3) e (852, 1147, 3)

img1 = cv2.resize(img1, (1147,852))
print(img1.shape)

# karıştırma işlemi burada olacak denklem mevcut. img1*alphaKatsayisi + img2*betaKatsayisi

blendedImage = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5,gamma= 0)
plt.figure()
plt.imshow(blendedImage )
























