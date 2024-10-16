# resimlere metin ve şekil ekleme üzerine çalışma 

import cv2
import numpy as np

# image generator 
img = np.zeros((512,512,3), np.uint8) # siyah resim olusturmaya yarayan dizin 
                                      # 512 512 3 bu resmin shape i 3 değil de 1 olsaydı renksiz olacaktı resim
print("Şeklin boyutu: ",img.shape)    # resmin boyutunu doğru ayarlamış mıyız diye kontrol ediyoruz 
#cv2.imshow("Numpy kutuphanesi tarafindan olusturulan goruntu: ", img) 

# resime çizgi ekleme konusunu ele alıyoruz
# sırasıyla (resim,baslangic noktasi,bitis noktasi,renk,kalinlik)
# renk muhabbetinde openCV de şu muhabbet var renk RGB değil de BGR şeklinde ilerliyor
cv2.line(img,(100,100),(200,200),(255,255,0),(5))
cv2.imshow("Cizgi", img)

#dikdortgen olusturmaya basliyoruz
#rectangle fonksiyonu ingilizcesinden de anlasilabilecegi uzere dikdortgen ciziminde kullaniliyor 
# siralamasi su sekilde (resim, baslangic pixeli,bitis pixeli, renk, kalinlik)
cv2.rectangle(img, (0,0),(256,256) , (255,0,0), cv2.FILLED) # cv2.FILLED ile dikdortgenin icerisini doldurabiliriz
cv2.imshow("dikdortgen", img)                               # kalinlik eklemek istersem cv2.FILLED yerine direk kalınlik pixelini yazabilirim (5 gibi)

# cember kismini inceleyelim
# bu fonksiyonda ise parametreler şu şekilde (resim, baslangic noktasi yani merkez, yaricap, renk  )
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED) # icerisini doldurma mantigi dikdortgen ile ayni 
cv2.imshow("circle", img)