# resimlere metin ve şekil ekleme üzerine çalışma 

import cv2
import numpy as np

# image generator 
img = np.zeros((512,512,3), np.uint8) # siyah resim olusturmaya yarayan dizin 
                                      # 512 512 3 bu resmin shape i 3 değil de 1 olsaydı renksiz olacaktı resim
print("Şeklin boyutu: ",img.shape)    # resmin boyutunu doğru ayarlamış mıyız diye kontrol ediyoruz 
cv2.imshow("Numpy kutuphanesi tarafindan olusturulan goruntu: ", img) 

