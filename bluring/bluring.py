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
plt.axis("off")
plt.show()





































