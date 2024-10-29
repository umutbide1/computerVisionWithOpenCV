# Görüntüye düşük geçirgenli bir filtre geçirerek parazit gidericez
# ortalama gürültü gidermeyi işliyoruz öncelikle
# şimdi şunu düşün 1080 e 1080 bir resim var ve bu resimde bazı yerler bozuk olsun
# bu bozuk yerleri bir filtre ile gezerek ortalamasını alacağız ve bozuk olan kısımı diğer doğru olan kısımla bastıracağız
# 1080*1080 bir görüntüyü 5*5 lik bir filtre ile gezelim mesela daha sonrasında her 5 e 5 de ortalama alarak ilerleyelim
# ortalama almak bu görüntüdeki paraziti yok edecektir

# Gauss çekirdeği ile bulanıklaştırma muhabbeti de var 

# medyan bulanıklaştırma da var bunları deneyelim bakalım 

import cv2
import matplotlib.pyplot as plt 
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# bluring detay azaltılır ve gürültü engellenir 

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("on")
plt.show()

# ortalama bluring i gerçekleyelim

img2 = cv2.blur(img, (3,3))
plt.figure() , plt.imshow(img2) , plt.axis("off") ,plt.title("ortalama blur"), plt.show()


# gauss noise ekleme kısmı 

gaussianBlur= cv2.GaussianBlur(img, (3,3), sigmaX=7)
plt.figure(), plt.imshow(gaussianBlur), plt.axis("off"), plt.title("gaussian blurlu durum"), plt.show()


# medyan blur, bu da ortalama yerine kutucukların medyanını alacaktır

medianBlur= cv2.medianBlur(img, (3))
plt.figure(), plt.imshow(medianBlur), plt.axis("off"), plt.title("Median Blur eklenmis durum"), plt.show()















































