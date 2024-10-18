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
           

