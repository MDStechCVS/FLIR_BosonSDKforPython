import numpy as np
import cv2, time
import traceback
import os.path
import threading

class VideoUtilsClass():
    def __init__(self, windows, videoNum, fps):
        self.windows = windows
        self.videoNum = videoNum
        # self.frame = frame              # 화면 보여주는 QLabel - frame
        self.fps = fps                  # 영상 프레임 수
        self.videInit = False
        self.cpt = None
        self.thread_trigger =True
        self.cap_trigger = False

        # Video 녹화
        self.fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        self.out = None
        self.width = None
        self.Height = None
        self.videoWriteNow = False
        self.captureName = 'N/A'

        # 이미지 상하, 좌우 반전
        self.flipVertical = False       # 위아래 반전
        self.flipHorizontal = False     # 좌우 반전
        self.lock = threading.Lock()


    def __del__(self):
        print(f"video {self.videoNum} 객체 삭제")
        

    def image_thread(self, window_num):
        if self.videInit == True:
            print("VideoView.py: startVideo() - 이미 영상이 연결되어 있습니다.")
            return
        else:
            self.cpt = cv2.VideoCapture(window_num)
            self.cpt.set(cv2.CAP_PROP_FPS, self.fps)
            
            if self.cpt != None:
                self.videInit = True
        self.windows.log_write(f"cam{window_num} start!")
        cnt = 0
        while True:
            try:
                cnt += 1 
                tr, self.cam = self.cpt.read()
                if tr == False:
                    print(f"window_num{window_num} is None")
                    continue
                self.windows.show_img(self.cam, window_num)
                    
                if self.videoWriteNow == True:
                        if self.out != None:
                            self.out.write(self.cam) 
                            
                if self.cap_trigger:
                    filename = self.fileName(1)
                    dirpath = f'./save/image/CAM{window_num}'
                    os.makedirs(f'{dirpath}', exist_ok=True)
                    cv2.imwrite(f'{dirpath}/{filename}', self.cam)
                    self.cap_trigger = False
                time.sleep(0.05)
            except Exception as e:
                print(f"Error code = {traceback.format_exc()}")
                pass
        

    def videoResume(self):
        if self.videInit == True:
            pass
        else:
            print("VideoView.py: videoResume() - cv2.VideoCapture가 활성화 되지 않았습니다")


    def videoFreeze(self):
        if self.videInit == True:
            pass
        else:
            print("VideoView.py: videoFreeze() - cv2.VideoCapture가 활성화 되지 않았습니다")


    def fileName(self, var):
        videoOrCapture = None
        if var == 0:
            videoOrCapture = 'BosonVideo_{}{}{}_{}{}{}.avi'
        elif var == 1:
            videoOrCapture = 'BosonCapture_{}{}{}_{}{}{}.png'

        t = time.localtime()
        fileName = videoOrCapture.format(t.tm_year,
                                         str(t.tm_mon).zfill(2),
                                         str(t.tm_mday).zfill(2),
                                         str(t.tm_hour).zfill(2),
                                         str(t.tm_min).zfill(2),
                                         str(t.tm_sec).zfill(2))
        return fileName


    def takeSnapShot(self):
        rValue = -1
        captureName = 'N/A'
        if self.videInit == True:
            captureName = self.fileName(1)
            # 캡쳐할때 아래 코드가 없으면 이미지가 색생이 반전되서 출력된다.
            self.cam = cv2.cvtColor(self.cam, cv2.COLOR_BGR2RGB)
            cv2.imwrite(captureName, self.cam, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
            # 파일 존재 여부 확인
            if os.path.isfile(captureName):
                rValue = 0
            print(f"CAMERA{self.videoNum} Take Shot")
        else:
            print("VideoView.py: takeSnapShot() - cv2.VideoCapture가 활성화 되지 않았습니다")
        return rValue, captureName


    def videoCapture(self):
        rValue = -1
        rValueCaptureName = 'N/A'
        if self.videInit == True:       # 비디오 스트리밍 중인지????
            if self.videoWriteNow == False:     # 현재 녹화 중이 아니라면
                # 녹화 시작
                self.captureName = self.fileName(0)
                dirpath = f'./save/video/CAM{self.videoNum}'
                os.makedirs(f'{dirpath}', exist_ok=True)
                output_path = f"{dirpath}/{self.captureName}"
                # 중간에 fps값을 인자값으로 정하는데 반드시 현재 카메라의 프레임 수와 동일 해야 한다.
                # 만약 다르면 녹화된 영상의 영상 속도가 느리거나 빠르게 보여진다.
                # self.out = cv2.VideoWriter(output_path, self.fourcc, float(self.fps), (self.cam.shape[1], self.cam.shape[0]))
                self.out = cv2.VideoWriter(output_path, self.fourcc, float(self.fps), (self.cam.shape[1], self.cam.shape[0]))
                self.videoWriteNow = True
                rValueCaptureName = 'Start Video capture'   # 리턴 문구에 비디오녹화가 시작되었다고 알려줌
                rValue = 0
                print(f"VIDEO{self.videoNum} RECORDING START")
                
            else:
                # 녹화 끝
                self.videoWriteNow = False

                if self.out != None:
                    self.out.release()
                    rValueCaptureName = self.captureName    # 리턴 문구에 현재 녹화된 비디오 파일 이름을 넘겨줌

                self.captureName = 'N/A'
                rValue = 1
        return rValue, rValueCaptureName


    def setFpsValue(self, val):
        self.fps = val


    def setVerticalTrueFalse(self, val):
        self.flipVertical = val       # 위아래 반전


    def setHorizontalTrueFalse(self, val):
        self.flipHorizontal = val       # 좌우 반전



        
        
