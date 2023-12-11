import os
import cv2
import time
import datetime
import natsort
import numpy as np
import serial.tools.list_ports
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.gridlayout import GridLayout
from UTIL.BosonCamAPI import BosonCamAPI as Boson
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class OpenCVCamera(Image):
    def __init__(self, capture, camera_index, **kwargs):
        super(OpenCVCamera, self).__init__(**kwargs)
        self.capture = capture
        self.capture_trigger = False
        self.stream = False
        self.camera_index = camera_index
        self.temp_trigger = False
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # 30 FPS


    def update(self, dt):
        if self.stream:
            ret, frame = self.capture.read()
            if self.capture_trigger == True:
                save_path = self.save_info()
                cv2.imwrite(f"{save_path}", frame)
                print(f"save_path = {save_path}")
                self.capture_trigger = False
            if ret:
                # 카메라 프레임을 텍스처로 변환
                buf = cv2.flip(frame, 0).tostring()
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.texture = texture


    def save_info(self):
        folder_path = f'./save/{self.camera_index}'
        os.makedirs(folder_path,  exist_ok = True)
        save_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S.%f')
        return f"{folder_path}/{save_time}.jpg"


class CameraWidget(BoxLayout):
    def __init__(self, camera_index, **kwargs):
        super(CameraWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(camera_index)
        self.camera_view = OpenCVCamera(self.capture, camera_index)
        self.add_widget(self.camera_view)
        button_layout = BoxLayout(size_hint_y=None, height='48dp', orientation='horizontal')
        # 스트리밍 버튼
        self.stream_button = Button(text=f'Streaming', size_hint_x=0.5)
        self.stream_button.bind(on_press=self.toggle_streaming)
        button_layout.add_widget(self.stream_button)

        


        # 캡처 버튼
        self.capture_button = Button(text='Capture', size_hint_x=0.5)
        self.capture_button.bind(on_press=self.capture_image)  # capture_image 함수 구현 필요
        button_layout.add_widget(self.capture_button)
        # 버튼 레이아웃을 CameraWidget에 추가
        self.add_widget(button_layout)


    def capture_image(self, instance):
        self.camera_view.capture_trigger = True


    def toggle_streaming(self, instance):
        self.camera_view.stream = not self.camera_view.stream
        if self.camera_view.stream:
            self.stream_button.text = f'Stop'
        else:
            self.stream_button.text = f'Streaming'



class CameraGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(CameraGridLayout, self).__init__(**kwargs)
        self.port_list = []
        self.cols = 2
        self.spacing = [10, 10]
        self.connect_state = False
        self.CAM = None
        self.port = None
        self.prod_num = None
        self.cam_obj = [None,None,None,None]
        self.spinner_idx = 0
        # Create left layout for cameras
        left_layout = GridLayout(cols=2)
        self.camera_grid = GridLayout(cols=2)
        self.camera_grid.spacing = [10, 10]
        self.prepare_cameras(self.get_connected_cameras())
        left_layout.add_widget(self.camera_grid)
        # Create right layout for spinner and buttons
        right_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=200, spacing=10)

        # Spinner for selecting cameras
        self.cameras = self.get_connected_cameras()
        self.spinner = Spinner(
            text='Select Camera',
            values=self.cameras,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': .5},
            background_color=[0.33, 0.50, 0.83, 1]
        )
        self.spinner.bind(text=self.on_spinner_text)
        
        # Buttons for various actions
        self.Connect_button = Button(text='Connect', size_hint=(None, None), size=(80, 50))
        self.FFC_button = Button(text=' Do\nFFC', size_hint=(None, None), size=(80, 50))



        whitehot_button = Button(background_normal='./res/whitehot.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(100, 400))  # 버튼 위치 (X, Y)
        whitehot_button.bind(on_press=lambda instance: self.change_palette(p_index=0))



        rainbowhc_button = Button(background_normal='./res/blackhot.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(220, 400))  # 버튼 위치 (X, Y)
        rainbowhc_button.bind(on_press=lambda instance: self.change_palette(p_index=1))


        rainbow_button = Button(background_normal='./res/rainbow.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(100, 500))  # 버튼 위치 (X, Y)
        rainbow_button.bind(on_press=lambda instance: self.change_palette(p_index=2))



        lava_button = Button(background_normal='./res/rainbowhc.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(220, 500))  # 버튼 위치 (X, Y)
        lava_button.bind(on_press=lambda instance: self.change_palette(p_index=3))



        ironbow_button = Button(background_normal='./res/ironbow.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(100, 600))  # 버튼 위치 (X, Y)
        ironbow_button.bind(on_press=lambda instance: self.change_palette(p_index=4))


#=====================================================================================
        hottest_button = Button(background_normal='./res/lava.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(220, 600))  # 버튼 위치 (X, Y)
        hottest_button.bind(on_press=lambda instance: self.change_palette(p_index=5))

        gradefire_button = Button(background_normal='./res/arctic.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(100, 700))  # 버튼 위치 (X, Y)
        gradefire_button.bind(on_press=lambda instance: self.change_palette(p_index=6))

        globow_button = Button(background_normal='./res/globow.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(220, 700))  # 버튼 위치 (X, Y)
        globow_button.bind(on_press=lambda instance: self.change_palette(p_index=7))
        
        blackhot_button = Button(background_normal='./res/gradefire.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(100, 800))  # 버튼 위치 (X, Y)
        blackhot_button.bind(on_press=lambda instance: self.change_palette(p_index=8))

        arctic_button = Button(background_normal='./res/hottest.jpg',
                              size_hint=(None, None),
                              size=(80, 80),  # 버튼 크기
                              pos=(220, 800))  # 버튼 위치 (X, Y)
        arctic_button.bind(on_press=lambda instance: self.change_palette(p_index=9))

        # Bind the Connect_button to the camconnect function
        self.Connect_button.bind(on_press=self.camconnect)
        self.FFC_button.bind(on_press=self.camffc)
        # Create a GridLayout for buttons
        button_grid = GridLayout(cols=2, spacing=(5, 5))
        # Add buttons to the GridLayout
        button_grid.add_widget(self.Connect_button)
        button_grid.add_widget(self.FFC_button)
        button_grid.add_widget(whitehot_button)
        button_grid.add_widget(rainbowhc_button)
        button_grid.add_widget(rainbow_button)
        button_grid.add_widget(lava_button)
        button_grid.add_widget(ironbow_button)
        button_grid.add_widget(hottest_button)
        button_grid.add_widget(gradefire_button)
        button_grid.add_widget(globow_button)
        button_grid.add_widget(blackhot_button)
        button_grid.add_widget(arctic_button)
        right_layout.add_widget(self.spinner)
        right_layout.add_widget(button_grid)
        self.add_widget(left_layout)
        self.add_widget(right_layout)


    def on_spinner_text(self, instance, text):
        self.spinner_idx = instance.values.index(text)
        print(f"Spinner Seleted : {self.spinner_idx}")


    def change_palette(self, p_index):
        try:
            rvalue = self.CAM.colorLutSetId(p_index)
            if rvalue:
                print("palette change Complete")
            else:
                print("palette change Incomplete")
        except Exception as e:
            print(f"카메라를 확인해주세요 {e}")


    def camffc(self, instance):
        try:
            rvalue = self.CAM.bosonRunFFC()
            if rvalue:
                print("Camera FFC Mode Complete")
            else:
                print("Camera FFC Mode incomplete")
        except Exception as e:
            print(f"카메라를 확인해주세요 {e}")

        
    def camconnect(self, instance):
        if self.connect_state == True:
            self.connect_state = False
            self.CAM.close()
            print(f"{self.port} Closed")
            self.Connect_button.text = 'Connect'
            self.spinner.disabled  = False
        else:
            self.port = self.spinner.text[7:]
            if "COM" in self.port:
                self.CAM = Boson(self.port)
                serial = self.CAM.getSerialNumber()
                self.prod_num = self.CAM.bosonGetCameraPN()
                self.Connect_button.text = 'Disconnect'
                self.connect_state = True
                self.spinner.disabled  = True
            else:
                self.show_warning_popup('Check Your Port')


    def show_warning_popup(self, text):
        content = BoxLayout(orientation='vertical')
        warning_label = Label(text=f"{text}")
        close_button = Button(text="Close")
        content.add_widget(warning_label)
        content.add_widget(close_button)

        # Define the function to close the popup
        def close_popup(instance):
            popup.dismiss()
        
        # Bind the close function to the button's on_press event
        close_button.bind(on_press=close_popup)

        # Define the popup object here so that it can be accessed inside close_popup
        popup = Popup(title="Warning", content=content, size_hint=(None, None), size=(400, 200))
        popup.open() 
            
     
    def prepare_cameras(self, connected_cameras ):
        cameras_to_create = min(len(connected_cameras), 4)
        for i in range(cameras_to_create):
            try:
                self.cam_obj[i] = CameraWidget(camera_index = i )
                self.camera_grid.add_widget(self.cam_obj[i])
                time.sleep(0.01)
            except Exception as e:
                self.camera_grid.add_widget(Label(text=f'Camera {i} Error: {e}'))
        for i in range(4 - cameras_to_create):
            self.camera_grid.add_widget(Label(text='No Camera'))

    def get_connected_cameras(self):
        ports = serial.tools.list_ports.comports()
        available_ports = []
        for idx, port in enumerate(ports):
            if port.serial_number == None:
                continue
            available_ports.append(f"{port.serial_number} {port.device}")
            self.port_list.append(port.device)
        print(f"available_ports = {available_ports}")
        available_ports = natsort.natsorted(available_ports)
        return available_ports


class CameraApp(App):
    def build(self):
        return CameraGridLayout()

if __name__ == '__main__':
    CameraApp().run()
    