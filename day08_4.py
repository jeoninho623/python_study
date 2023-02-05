import cv2
import mediapipe as mp

cap = cv2.VideoCapture('person.jpg')                    # 0으로 시작하면 웹캠
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
# 50% 얼굴이면 얼굴로 인식
fd = mp_fd.FaceDetection(0.9)  

# 읽은 비디오를 여러개의 이미지로
success, img = cap.read()
# 색보정 (정확도)
from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 얼굴을 찾아줘
result = fd.process(from_bgr_to_rgb)

#얼굴 찾으면
if result.detections:
    # 각 얼굴별로
    for id, detecion in enumerate(result.detections):
        mp_draw.draw_detection(img, detecion)       # 네모표시

# 보여주고 기다려
cv2.imshow('title.jpg',img)
cv2.waitKey(0)