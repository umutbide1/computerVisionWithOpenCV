import cv2 

cap=cv2.VideoCapture(0)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

# video kaydedici kısmı 

writer= cv2.VideoWriter("video_kaydi_deneme.mp4",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height)) # cerceveleri sikistirmak icin kullanilan kodec kodu imis fourcc kismi

#video kaydetme kismi vesaire 

while True:
    ret,frame = cap.read()
    cv2.imshow("video",frame)
    
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q") : break

cap.relase()
writer.relase()
cv2.destroyAllWindows()