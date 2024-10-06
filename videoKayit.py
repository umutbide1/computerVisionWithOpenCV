import cv2 

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

# Video kaydedici kısmı
writer = cv2.VideoWriter("video_kaydi_deneme.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width, height))

# Video kaydetme kısmı
while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)

    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break

# Kaynakları serbest bırakma kısmı
cap.release()  # relase değil release olmalı
writer.release()  # relase değil release olmalı
cv2.destroyAllWindows()
