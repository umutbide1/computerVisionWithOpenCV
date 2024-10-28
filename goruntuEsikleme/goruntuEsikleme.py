import cv2
import matplotlib.pyplot as plt
 # Normalde genlik değerleri 0-255 arasında gidiyor mesela Biz bu eşik değerini değiştirerek istediğimiz nesneleri 
 # biraz daha belirgin hale getirip bu genliğin altındaki pixelleri ise direkt yok edeceğiz.

img= cv2.imread("img1.jpg",0)
plt.figure()   
plt.imshow(img , cmap="gray") # burada ise color map i değiştirip tam bir siyah beyaz görüntü elde ediyorum
plt.axis("off")
plt.show() # normalde bu yazılmasa bile Spyder ekrana görüntüyü alıyor ama normalde almaması lazım 
           # bu plt.imshow() sadece koordinat sistemine resmi yerleştiriyor göstermeyi yapmıyor 
           # ama bu işlem cv2.imshow() da aynı değil cv2 de hem görüntüyü yerleştiriyor hemde ekrana basıyor
           # cv2 da görüntü formatı BGR matplotlib de ise RGB şeklinde 
           
# şimdi fotoğrafın genlik değerini 0 255 den 0 60 çekeceğim

_, thresh_img= cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY) # bu satırı aşağıda açıklıyorum
# en sağda bulunan BINARY kısmında 60 la 255 arasındaki genlik değerlerini beyaz yapacak THRTHRESH_BINARY_INV kullansaydım 
                                                                                        # tam tersi siyah yapardı
plt.show()         
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")           
plt.show()                                                

# img=cv2.resize(img,(800,600))
# cv2.imshow("anaResim", img)

# adaptif bir eşikleme yapacağız şuan çünkü şöyle bir durum var mesela dağı ayırabildik ama bir kısmını ayırabildik hepsini
# ayıramadık bu mantıklı değil çünkü dağın bütünlüğünü bozduk şimdi adaptif şekilde bunun bütünlüğünü bozmamaya bakalım

thresh_img= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()
# harika önemli bölgeler harika bir biçimde ayrılmış biçimde 
