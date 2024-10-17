import cv2 
import pandas as pd
import numpy as np
img= cv2.imread("kart.png")
cv2.imshow("Kart", img)

width=500
height=600
# kartın 4 köşesini bulmaya çalışacağız 
# paintten bakıyoruz sol ust kose : 201 e 1    sağ üst kose : 541 146   sag alt kose : 339 617  sol alt kose : 1 472 

point1= np.float32([[201,1],[1,472],  # bura benim yamuk resmimin kenarlarının denk geldiği pixel kısımları
                    [541,146],[339,617]]) 

point2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

transformMatris = cv2.getPerspectiveTransform(point1, point2)   # transform matris hesabının yapılması
print(transformMatris) # burada transform matrisin değerleri alınabilir

imgLastStatus = cv2.warpPerspective(img, transformMatris, (width,height)) 
cv2.imshow("Son Durum", imgLastStatus)
