import cv2


img= cv2.imread("messi.jpg",0)
img2=cv2.imread("messi2.jpg",1)

cv2.imshow("ilk resim", img)
cv2.imshow("ikinci resim",img2)

k= cv2.waitKey(0) &0xFF

if k==27 :# 27 burada esc tuşuna karşılık gelmekte
    cv2.destroyAllWindows()
    
elif k== ord("s"): # bu da bildiğimiz save anlamına gelen s tuşumuz
    cv2.imwrite("siyahBeyazMessi2.png",img2)
    cv2.destroyAllWindows()

