# opencv 모듈추가
# mediapipe 모듈추가


# 웹캠 얼굴찾기

import cv2
import mediapipe as mp

# 이미지 (좌측 상단에 내 이름)
# def ShowImage(img_path):
#     img = cv2.imread(img_path)
#     cv2.putText(img,'jeon inho',(0,50),cv2.FONT_ITALIC,1,(0,0,0),2)
#     cv2.imshow('title',img)
#     cv2.waitKey(0)

# ShowImage('person2.jpg')

# 동영상 (좌측상단에 크기조정 resize)
def ShowVideo(video_path):
    video = cv2.VideoCapture('person2.mp4')

    mp_fd = mp.solutions.face_detection
    mp_draw = mp.solutions.drawion_utils
    fd = mp_fd.FaceDetection()

    while True:
        success, img = video.read()
        img = cv2.resize(img, (900,640))
        if success:
            from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)          
            face = fd.process(from_bgr_to_rgb)             

        if face.detections:
            for id, detection in enumerate(face.detections):
                fd_box=detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]),\
                     int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
                cv2.rectangle(img, box, (47,230,53),2)      
                cv2.putText(img, f'{round(detection.score[0]*100,2)}%',(box[0],box[1])\
                    ,cv2.FONT_ITALIC,2,(47,230,53),1)


ShowVideo('person2.mp4')