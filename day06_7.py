# import가 안되는 이유 : 설치가 안된 라이브러리(모듈) 또는 오타
# 외부 모듈 설치 : pip imstall 모듈명

# pip install python-opencv              (일반 파이썬)
# pip install opencv-python              (아나콘다 파이썬)
import cv2

# 이미지 = cv2.imread('img1.png')           # 이미지를 읽어줘
# cv2.imshow('title',이미지)                # 보여줘

# cv2.waitKey(0)                            # 무한대기

def cv_img(path):
    코끼리 = cv2.imread('ele.jpg')
    cv2.imshow('title',코끼리)
    cv2.waitKey(0)

cv_img('ele.jpg')