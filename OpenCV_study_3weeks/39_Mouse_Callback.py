# 콜백(Callback) 함수-매개 변수를 통해 다른 함수를 전달 받고, 이벤트가 발생할 때 매개 변수에 전달된 함수를 호출하는 역할
# 특정한 이벤트가 발생하면 다른 함수를 실행하는 함수

import cv2
import numpy as np


def mouse_event(event, x, y, flags, param):
    """
    event-윈도우에서 발생하는 이벤트를 의미
    x, y-마우스의 좌표를 의미
    flags-event와 함께 활용되는 역할(특수한 상태를 확인하는 용도)
    param-마우스 콜백 설정 함수에서 함께 전달되는 사용자 정의 데이터를 의미
    """
    
    global radius   # 전역변수로 선언
    
    # event가 왼쪽 마우스 클릭이 발생했을 때 윈도우에 파란색 원을 그립니다.
    if event == cv2.EVENT_FLAG_LBUTTON:    
        cv2.circle(param, (x, y), radius, (255, 0, 0), 2)
        cv2.imshow("draw", src)

    # event가 마우스 스크롤을 조작
    # event가 마우스 스크롤 이벤트일 때, flag는 마우스 스크롤의 방향
    # flag = 양수-스크롤 업 / 음수-스크롤 다운
    # 마우스 스크롤 업 이벤트-반지름(radius)를 증가, 다운 이벤트-반지름을 감소
    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            radius += 1
        elif radius > 1:
            radius -= 1
# 반지름(radius)를 저장할 변수, 원본 이미지(src)를 선언
# radius-마우스 콜백 함수에서 마우스 스크롤에 따라, 값을 증가하거나 감소
radius = 3
src = np.full((500, 500, 3), 255, dtype=np.uint8)

# cv2.namedWindow() / cv2.imshow() 를 활용하여 윈도우를 생성
cv2.imshow("draw", src)
# 우스 콜백 설정 함수(cv2.setMouseCallback)로 마우스 콜백을 설정
# cv2.setMouseCallback(윈도우, 콜백 함수, 사용자 정의 데이터)
cv2.setMouseCallback("draw", mouse_event, src)
"""
윈도우-미리 생성되어 있는 윈도우의 이름을 의미
콜백 함수-마우스 이벤트가 발생했을 때, 전달할 함수를 의미
사용자 정의 데이터-마우스 이벤트로 전달할 때, 함께 전달할 사용자 정의 데이터를 의미
"""
cv2.waitKey()