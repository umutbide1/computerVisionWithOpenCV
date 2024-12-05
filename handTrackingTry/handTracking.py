import cv2
import mediapipe as mp

# MediaPipe modüllerini başlatalım
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_detection

# Parmakların isimleri (başparmak hariç)
finger_names = ['İşaret', 'Orta', 'Yüzük', 'Serçe']

# Parmak sayma fonksiyonu
def count_fingers(hand_landmarks, hand_label):
    finger_count = 0

    # Elin hangi yönde olduğunu belirlemek için
    if hand_label == 'Right':
        is_right = True
    else:
        is_right = False

    # Başparmak için
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    # Başparmağın açık olup olmadığını kontrol et
    if is_right:
        if thumb_tip.x < thumb_ip.x:
            finger_count += 1
    else:
        if thumb_tip.x > thumb_ip.x:
            finger_count += 1

    # Diğer parmaklar için
    finger_tips = [
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
    ]

    finger_pips = [
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP],
    ]

    # Her parmak için kontrol et
    for tip, pip in zip(finger_tips, finger_pips):
        if tip.y < pip.y:
            finger_count += 1

    return finger_count

# Video yakalamayı başlatalım (0, varsayılan kamerayı temsil eder)
cap = cv2.VideoCapture(0)

# El ve yüz tanıma modüllerini başlatalım
with mp_hands.Hands(
    max_num_hands=2,  # Algılanacak maksimum el sayısı
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands, \
     mp_face.FaceDetection(
    min_detection_confidence=0.7) as face_detection:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Kameradan görüntü alınamadı.")
            break

        # Görüntüyü yatay olarak çevirip BGR'den RGB'ye dönüştürelim
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image_height, image_width, _ = image.shape  # Görüntü boyutları

        # El ve yüz algılama işlemlerini yapalım
        hand_results = hands.process(image_rgb)
        face_results = face_detection.process(image_rgb)

        # İşaretlemeleri çizelim
        # Yüzler
        if face_results.detections:
            for detection in face_results.detections:
                # Yüz algılama sonuçlarını çizelim
                mp_drawing.draw_detection(image, detection)

        # Eller
        if hand_results.multi_hand_landmarks:
            for hand_landmarks, hand_info in zip(hand_results.multi_hand_landmarks, hand_results.multi_handedness):
                # Eklemleri ve bağlantıları çizelim
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Elin hangi yönde olduğunu alalım (Sağ veya Sol)
                hand_label = hand_info.classification[0].label

                # Parmak sayısını hesaplayalım
                finger_count = count_fingers(hand_landmarks, hand_label)

                # Sonucu görüntüye yazdıralım
                cv2.putText(image, f'{hand_label} - Parmak Sayisi: {finger_count}', (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

        # Görüntüyü gösterelim
        cv2.imshow('El ve Yuz Takip', image)

        # 'q' tuşuna basıldığında çıkalım
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
