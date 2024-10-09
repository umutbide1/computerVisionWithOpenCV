import cv2

img = cv2.imread("lenna.png",0) # ikinci parametreyi vermezsen görüntü ekrana renkli yansiyacaktir.
                                #ikinci parametre 0 oldugunda ise goruntu siyah beyaz formatta olacaktir.
print("resim boyutu: ", img.shape) # shape fonksiyonu ile resmin pixel boyutlarini ogreniyoruz 
cv2.imshow("orijinal", img) # burada image i ismi ile ekrana süren komutu yazıyoruz

imgResized= cv2.resize(img, (800,800))  # herhangi bir resmi yeniden boyutlandırmanın kodu enteresan doğrusu ilk defa yapan için
print("Resmin yeni boyutu: ", imgResized.shape)  #burada yeni resmimizin boyutları doğru mu diye kontrol ediyoruz

cv2.imshow("Resize edilmis yeni goruntu: ", imgResized) # burada da yeniden boyutlandırılmış görselin çıktısı var.


# Simdi de kırpma kısmını bir inceleyelim 
