import cv2

#비디오 출력 클래스(cv2.VideoCapture)를 통해 내,외장 카메라에서 정보를 받아옴
#cv2.VideoCapture(index)로 카메라의 장치 번호(ID)와 연결
#index는 카메라의 장치 번호를 의미"""

#외장 카메라를 사용하는 경우, 장치 번호가 1~n

capture = cv2.VideoCapture(0)

#카메라 속성 설정 메서드(capture.set)로 카메라 속성 설정
#capture.set(propid, value)로 카메라의 속성(propid)과 값(value)을 설정
#propid은 변경하려는 카메라 설정을 의미
#value은 변경하려는 카메라 설정의 속성값을 의미"""

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#키 입력 대기 함수(cv2.waitkey)는 지정된 시간 동안 키 입력이 있을 때까지 프로그램을 지연
#cv2.waitkey(delay)로 키 입력을 기다림. delay는 지연 시간을 의미(밀리 초 단위)
"""키 입력 대기 함수는 입력된 키의 아스키 코드 값을 반환
    즉, 어떤 키라도 입력되기 전까지 33ms마다 반복문을 실행
        Tip : delay가 0일 경우, 지속적으로 키 입력을 검사하여 프레임이 넘어가지 않음.
        Tip : while cv2.waitKey(33) != ord('q'):으로 사용할 경우, q가 입력될 때 while문을 종료
"""
while cv2.waitKey(33) < 0:

    #프레임 읽기 메서드(capture.read)를 이용하여 카메라의 상태 및 프레임을 받아옴
    #ret은 카메라의 상태가 저장되며 정상 작동할 경우 True를 반환, 작동하지 않을 경우 False를 반환
    #frame에 현재 시점의 프레임이 저장

    ret, frame = capture.read()

    #이미지 표시 함수(cv2.imshow)를 이용하여 특정 윈도우 창에 이미지를 띄웁니다.

    cv2.imshow("VideoFrame", frame)

#메모리 해제 메서드(capture.relase)로 카메라 장치에서 받아온 메모리를 해제

capture.release()

#특정 윈도우 창만 닫는다면, cv2.destroyWindow(winname)

cv2.destroyAllWindows()