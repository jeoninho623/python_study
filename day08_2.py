import cv2

def ShowImage(img_path):
    # 이미지 읽어줘
    img = cv2.imread(img_path)
    # 이미지 보여줘
    cv2.imshow('Ganzi',img)
    # 대기
    cv2.waitKey(0)

def ShowVideo(video_path):
    # 동영상 읽어줘
    mp4 = cv2.VideoCapture(video_path)
    # 무한반복
    while True:
        # 읽기성공여부, 동영상을 자른 이미지
        success, img = mp4.read()
        #동영상을 성공적으로 읽었으면
        if success:
            cv2.imshow('title',img)
        if cv2.waitKey(20) & 0xFF == 27:
            # 동영상 waitkey 20~25
            # ESC 키를 눌러 종료
            break

def ShowCam ():
    # 캠 읽어줘
    mp4 = cv2.VideoCapture(0)
    # 화면 조정
    mp4.set(3, 640)
    mp4.set(4, 480)
    # 무한반복 (동영상 == 빠르게 여러 이미지를 출력)
    while True:
        # 읽기성공여부, 자른 이미지
        success, img = mp4.read()
        #동영상을 성공적으로 읽었으면
        if success:
            cv2.imshow('title',img)
        if cv2.waitKey(1) & 0xFF == 27:
            # 캠 : waitkey 1
            # ESC를 눌러 종료
            break

# ShowImage('person.jpg')
ShowVideo('person.mp4')
