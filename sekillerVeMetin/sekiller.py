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
cv2.line(img,(0,0),(512,512),(255,0,0),(5))      
cv2.imshow("Çizgi", img)           

