import cv2
import numpy as np

def gamma_correction(cap, c=1, g=5):
    out = cap.copy()
    # out /= 100.
    out = (1 / c * out) ** (1 / g)
    out *= 250
    out = out.astype(np.uint8)
    return out
num = 0

cap = cv2.VideoCapture('C111100_003.avi')

fps = 30.0  # fps
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1280  # 영상 가로 길이
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 720  # 영상 세로 길이

fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 지정
writer = cv2.VideoWriter('output5.avi', fourcc, fps, (width, height))
#(저장될 동영상 파일 이름, 코덱, 영상의 초당 프레임수, 이미지 크기 캡쳐되는 이미지와 일치시키기)

while (cap.isOpened()):  # 비디오 스트림이 열려 있으면
    ret, img = cap.read() # ret과 img를 얻고
    if ret == False:  # 끝이라면 프로그램 종료
        break;

    print(num ,' %')
    num = num + 1

    writer.write(gamma_correction(img))
else:
    print("비디오를 열 수 없음")

# cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
