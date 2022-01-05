import cv2
import numpy as np
import matplotlib.pyplot as plt


def gamma_correction(cap, c=1, g=5):
    out = cap.copy()
    # out /= 100.
    out = (1 / c * out) ** (1 / g)
    out *= 150
    out = out.astype(np.uint8)
    return out


videofile = "C:/Users/user/PycharmProjects/g/C102100_022.mp4"
cap = cv2.VideoCapture(videofile)  # // 비디오 스트림을 가져온다.

fps = 30.0  # fps
width = 1280  # 영상 가로 길이
height = 720  # 영상 세로 길이
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 'm', 'p', '4', 'v' 코덱 적용
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))  # 비디오 저장을 위한 객체 생성

while (cap.isOpened()):  # 비디오 스트림이 열려 있으면
    ret, frame = cap.read()  # ret과 img를 얻고
    # out = gamma_correction(frame)  # img 값에 필터를 씌운다.

    if ret:  # ret이 true라면
        cv2.imshow('video',frame)
        # out.write(img)  # 해당 영상을 저장
    else:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

# if cap.isOpened():
#     while True:
#         ret, img = cap.read()    
#         out = gamma_correction(img)
#         if ret:          
#             cv2.imshow("result", out)
#             cv2.waitKey(25)
#         else:                  
#             break              
# else:
#     print("can't open video.")

# cap.release()
# out.release()                
# cv2.destroyAllWindows()
