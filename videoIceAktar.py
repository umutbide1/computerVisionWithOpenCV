import cv2 
import time

video_name="MOT17-04-DPM.mp4"
#videoyu içe aktarma kısmı 
cap= cv2.VideoCapture(video_name)

print("genislik:", cap.get(3)) # genişlik 3. indexte bulunmakta 
print("yukseklik", cap.get(4)) # yükseklik ise 4. indexte bulunmakta
# cap içerisinde video var gibi görünsede bazen bu böyle olmayabilir hocam. Dikkatli olmak lazım
# bunun için ise capture içerisine hep göz atıyoruz if else komutlarıyla

if cap.isOpened()==False: # burası önemli
    print("Hata")
 
    
while True:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01) # kullanılmazsa görüntü korkunç hızlı akar 
        
        cv2.imshow("Video",frame)
        
    else:break
    
    if cv2.waitKey(1) &0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
        
