import cv2
import mediapipe as mp
import math

def distancia(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    text = ""

    if results.multi_hand_landmarks:
        hand_positions = []
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Obtener posiciones de muñeca y dedos
            wrist = hand_landmarks.landmark[0]
            wrist_y = int(wrist.y * h)
            hand_positions.append(wrist_y)

            # Coordenadas de los dedos
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            pinky_tip = hand_landmarks.landmark[20]

            # Convertir a píxeles
            thumb_tip_px = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            wrist_px = (int(wrist.x * w), int(wrist.y * h))

            # Detección de ME GUSTAS: puño cerrado y pulgar arriba
            dist_index = distancia(wrist_px, (int(index_tip.x * w), int(index_tip.y * h)))
            dist_middle = distancia(wrist_px, (int(middle_tip.x * w), int(middle_tip.y * h)))
            dist_ring = distancia(wrist_px, (int(ring_tip.x * w), int(ring_tip.y * h)))
            dist_pinky = distancia(wrist_px, (int(pinky_tip.x * w), int(pinky_tip.y * h)))

            if (dist_index < 60 and dist_middle < 60 and dist_ring < 60 and dist_pinky < 60 and
                thumb_tip_px[1] < wrist_px[1]):
                text = "ME GUSTAS"

        if len(hand_positions) == 2:
            y1, y2 = hand_positions
            if y1 < h // 2 and y2 < h // 2:
                text = "HOLA"
            elif y1 > int(h * 0.7) and y2 > int(h * 0.7):
                text = "CÓMO ESTÁS"

    if text:
        cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

    cv2.imshow("Lengua de Señas", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
