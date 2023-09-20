import logging
import traceback
import tkinter as tk
from  UTIL.Log_Util import Init_Logger
from UTIL.BosonCamInit import Make_Port_List, BosonCamInitClass as BOSON
from UTIL.Video import VideoUtilsClass
import cv2
from PIL import Image, ImageTk
from tkinter import ttk
import threading
import time


#logger
#=============================================
Init_Logger() # 로그 생성
trace = logging.getLogger("TRACE") # logger get
debug = logging.getLogger("DEBUG")
#=============================================


class MainWindow(tk.Frame):
    def __init__(self, master=None, ):
        super().__init__(master)
        self.master = master
        # 카메라 정보 담고있는 dictionary
        self.INFO = {
                    0: {'PORT': None, "CAMERA" : None, 'SN' : None, "R" : None, 'CONN' : None, 'PN' : None, "FPS" : None,},
                    1: {'PORT': None, "CAMERA" : None, 'SN' : None, "R" : None, 'CONN' : None, 'PN' : None, "FPS" : None,},
                    2: {'PORT': None, "CAMERA" : None, 'SN' : None, "R" : None, 'CONN' : None, 'PN' : None, "FPS" : None,},
                    3: {'PORT': None, "CAMERA" : None, 'SN' : None, "R" : None, 'CONN' : None, 'PN' : None, "FPS" : None,},
                    }
        
        #video thread 생성
        self.connected_cam = None
        # 배경색 설정
        self.configure(bg=bg_color)  
        # MAIN INDEX
        self.MAIN_INDEX = 0
        #top level trigger
        self.toplevel_open = False
        # 이미지 업데이트 윈도우 
        self.image_window = [None, None, None, None]
        self.setting_window = []
        # initialize update image
        self.bg_image = cv2.imread('./res/gray.png')
        # img_show함수 관련 변수
        self.cvtimg = [None, None, None, None]
        self.cvtshow = [None, None, None, None]
        self.updateImage = [None, None, None, None]
        self.back_cam = [None, None, None, None]
        self.updateImage_backup = [None, None, None, None]
        self.bufferImage = [None, None, None, None]
        # Text SERIAL / PORT
        self.text_ipinfo = "SERIAL / PORT"
        # widget init
        self.create_widgets()
        # mouse event 기능 bind 
        self.main_canvas.bind('<Button-1>', self.main_btn)
        self.main_canvas.pack(fill=tk.BOTH, expand=True)
        self.log_write('[INFO] Initialize Complete')
        trace.info('[INFO] Initialize Complete')
        

    #=======================================================================================================================================    
    # 위젯 생성 함수   
    def create_widgets(self):
        self.main_canvas = tk.Canvas(self, width=900, height=600, bg=bg_color) 
        self.main_canvas.grid(row=0, column=0)  

        # 캠 포트 리스트박스 생성
        self.listbox = tk.Listbox(self.main_canvas)  
        self.listbox.config(width = 27, height = 6)
        self.listbox.place(x = 660, y = 40)
        

        # 로그 리스트박스 생성
        log_frame = tk.Frame(self.main_canvas)
        log_frame.place(x=660, y=213)  # Frame을 원하는 위치에 배치
        self.logbox = tk.Listbox(log_frame, width=30, height=20, bg="white", fg="black", selectbackground="red")
        self.logbox.pack(side=tk.LEFT, fill=tk.BOTH)  # Frame 안에 Listbox 배치
        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Frame 안에 Scrollbar 배치
        self.logbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.logbox.yview)
        
        # Get PORT -> PORT 리스트박스 표시
        MP = Make_Port_List()
        self.info_list =MP.port_check()
        for idx, info in enumerate(self.info_list):
            port = info[0]
            serial = info[1]
            self.INFO[idx]['PORT'] = port
            self.INFO[idx]['SN'] = serial
            listbox_str = f"{serial} / {port} "
            trace.info(f"available port : {listbox_str}")
            # self.listbox.insert(tk.ACTIVE, item)
            self.listbox.insert(tk.END, listbox_str)
            
        # LISTBOX - main index 연결
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        # create text
        self.on_ipinfo = self.main_canvas.create_text(730, 25, text=self.text_ipinfo, font=('gothic', 13, 'bold'), fill='white', anchor='center')
    #=======================================================================================================================================
    
    

    # button 모음
    #=======================================================================================================================================    
        self.capture_button = tk.Button(self.main_canvas, text="CAPTURE", command=self.button_capture, width=8, height=3)
        self.capture_button.place(x = 660, y = 142)

        self.video_capture_button = tk.Button(self.main_canvas, text="VIDEO\nSTART", command=self.button_video_capture, width=8, height=3)
        self.video_capture_button.place(x = 725, y = 142)
        
        self.setting_button = tk.Button(self.main_canvas, text="Setting", command=self.button_setting, width=8, height=3)
        self.setting_button.place(x = 790, y = 142)
        
        self.up_button = tk.Button(self.main_canvas, text="▲", command=self.button_up, width=2, height=2)
        self.up_button.place(x = 855, y = 40)
        
        self.down_button = tk.Button(self.main_canvas, text="▼", command=self.button_down, width=2, height=2)
        self.down_button.place(x = 855, y = 80)
        
    
        

        

        #image update canvas 생성 
        self.image_window[0] = self.main_canvas.create_image(10, 20, image = '', anchor = 'nw')
        self.image_window[1] = self.main_canvas.create_image(335, 20, image = '', anchor = 'nw')
        self.image_window[2] = self.main_canvas.create_image(10, 280, image = '', anchor = 'nw')
        self.image_window[3] = self.main_canvas.create_image(335, 280, image = '', anchor = 'nw')
        
        # DIC에 PORT VLAUE 모두 확인 후 현재 붙은 카메라 수 확인
        cam_info = self.find_values_by_key("PORT")
        print(f"cam_info = {cam_info}")
        self.connected_cam = [x for x in cam_info if x is not None]
    #=======================================================================================================================================    
    
    
    
    # 카메라 관련 함수
    #=======================================================================================================================================
    # Boson 카메라 Connect 
    def connect(self):
        port =  self.INFO[self.MAIN_INDEX]['PORT'] 
        self.INFO[self.MAIN_INDEX]['CAMERA'] = BOSON(self,port)
        isConnect, PN = self.INFO[self.MAIN_INDEX]['CAMERA'].camConnect()
        if isConnect:
            self.INFO[self.MAIN_INDEX]['PN'] = PN
            if "R" in str(PN):
                self.INFO[self.MAIN_INDEX]['R'] = True
            self.INFO[self.MAIN_INDEX]['CONN'] = True
            print(f"boson api connect PORT = {port}")
            print(f"현재 index = {self.MAIN_INDEX}")


        
    def boson_disconnect(self):
        port = self.INFO[self.MAIN_INDEX]['PORT']
        rvalue = self.INFO[self.MAIN_INDEX]['CAMERA'].camClose()
        if rvalue:
            print(f"boson {port} Disconect")
    #=======================================================================================================================================
            

    
    # button 기능 함수 모음
    #=======================================================================================================================================
    def button_up(self):
        selected = self.listbox.curselection()
        index = selected[0]
        if index == 0:
            self.log_write(f"올릴 수 없습니다.")
            return
        rvalue = self.dic_value_change(index, index - 1)
        self.log_write(f"index => {index}  // index - 1 => {index - 1}")
        if rvalue:
            item = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index - 1, item)
            self.listbox.selection_set(index - 1)
        
        
    def button_down(self):
        selected = self.listbox.curselection()
        index = selected[0]
        rvalue = self.dic_value_change(index, index + 1)
        if index == self.listbox.size() - 1:
            self.log_write(f"내릴 수 없습니다.")
            return
        self.log_write(f"CAM{index} => CAM{index + 1}")
       
        
        if rvalue:
            item = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index + 1, item)
            self.listbox.selection_set(index + 1)
           

    def add_new_port(self,  new_port, serial):
        for key, value in self.INFO.items():
            if value['PORT'] is None:
                self.INFO[key]['PORT'] = new_port
                self.INFO[key]['SN'] = serial
                return True  # 성공적으로 새로운 포트를 추가했음을 나타냅니다.
        return False 
    
    
            
    def button_refresh(self):
        Rvalue = False
        MP = Make_Port_List()
        port_list =MP.port_check()
        print(f"port_list = {port_list}")
        DIC_PORT = self.find_values_by_key("PORT")
        print(f"DIC_PORT = {DIC_PORT}")
        for idx, value in enumerate(port_list):
            if value[0] not in DIC_PORT:
                port = value[0]
                serial = value[1]
                print(f"INFO = {self.INFO}")
                Rvalue = self.add_new_port(port, serial)
                if Rvalue:
                    listbox_str = f"{serial} / {port}"
                    self.listbox.insert(tk.END, listbox_str)
                    video_none_index = video_object.index(None)
                    video_object[video_none_index] = VideoUtilsClass(self, video_none_index, 15) # video class 생성
                    video_thread[video_none_index] = threading.Thread(target=video_object[video_none_index].image_thread,
                                                        args=(video_none_index,), daemon=True).start() # grab loop thread
                    time.sleep(0.05)
        
        print(f"INFO DIC = {self.INFO}")                


    def button_capture(self):
        video_object[self.MAIN_INDEX].cap_trigger = True
        self.log_write(f"cam{self.MAIN_INDEX} take picture!")
        print(f"cam{self.MAIN_INDEX} take picture!")

    
    def button_video_capture(self):
        print(f"check 1 : {self.INFO[self.MAIN_INDEX]['FPS']}")
        video_object[self.MAIN_INDEX].fps = self.INFO[self.MAIN_INDEX]['FPS']
        rValue, revCaptureName = video_object[self.MAIN_INDEX].videoCapture()
        if rValue == 0:
            self.video_capture_button.config(text="VIDEO\nSTOP")
            self.log_write(f"CAM{self.MAIN_INDEX} video record start")
            trace.info(f"CAM{self.MAIN_INDEX} video record start")
            print("video record start")
        elif rValue == 1:
            print("video record end")
            self.log_write(f"CAM{self.MAIN_INDEX} video record end")
            trace.info(f"CAM{self.MAIN_INDEX} video record end")
            self.video_capture_button.config(text="VIDEO")

    
    # setting 창 Open 버튼
    def button_setting(self):
        self.connect()
        self.show_toplevel()
        
        
    # setting 창 안에 doffc버튼
    def button_doffc(self, camera_index):
        print("DODODODO FFC!")
        rvalue = False
        rvalue = self.INFO[camera_index]['CAMERA'].doFFC()
        self.log_write(f"Changing palette CAM{camera_index} -> FFC ON")
        trace.info(f"Changing palette CAM{camera_index} -> FFC ON")
        return rvalue
    

    # setting 창 안에 radiometric버튼
    def button_temp(self):
        print("라디오메트릭 계산 중")
    #=======================================================================================================================================
        


        
        
    #Setting(toplevel) 관련 함수
    #======================================================================================================================================= 
    # toplevel UI Open & 버튼 생성 
    def show_toplevel(self):
        if not self.toplevel_open:
            self.toplevel_open = True
            # Create and configure the toplevel window
            index = self.MAIN_INDEX
            self.log_write(f'CAM{self.MAIN_INDEX} Setting Window Open')
            toplevel = tk.Toplevel(self)
            toplevel.title(f"{self.INFO[index]['SN']} / {self.INFO[index]['PORT']}")
            toplevel.geometry("800x600")
            toplevel.configure(bg="#04001f")
            toplevel.protocol("WM_DELETE_WINDOW", lambda: self.on_toplevel_close(toplevel))
            toplevel.iconbitmap('./res/logo.ico')

            #Do FFC button
            self.ffc_button = tk.Button(
                                        toplevel, 
                                        text="Do\nFFC", 
                                        command=lambda camera_index=self.MAIN_INDEX : self.button_doffc(self.MAIN_INDEX), 
                                        width=8, 
                                        height=3)
            self.ffc_button.place(x=35, y=160)  # 원하는 좌표에 배치

            #Radio metric Button
            if self.INFO[self.MAIN_INDEX]['R']:
                print(f"index  = {self.MAIN_INDEX} trigger = {self.INFO[self.MAIN_INDEX]['R']}")
                self.temp_button = tk.Button(
                                            toplevel, 
                                            text="Radio\nMetric", 
                                            command=self.button_temp, 
                                            width=8, 
                                            height=3
                                            )
                self.temp_button.place(x=120, y=160)  # 원하는 좌표에 배치
            
            #palette 버튼!
            palette_image_list = self.palette_image_path()
            
            self.make_photo_button(toplevel, palette_image_list, self.MAIN_INDEX)
         
         
    # palette 사진 로드 및 좌표 정리
    def make_photo_button(self, window ,path_list, camera_index ):
        for idx, path in enumerate(path_list):
            image = cv2.imread(path)
            resize_image = cv2.resize(image, (100,50))
            pil_image = Image.fromarray(cv2.cvtColor(resize_image, cv2.COLOR_BGR2RGB))
            image = ImageTk.PhotoImage(pil_image)
            image_button = tk.Button(window, 
                                     image=image, 
                                     command=lambda idx=idx, 
                                     camera_index = camera_index: self.change_palette(idx, camera_index) ,
                                     width=100, 
                                     height=50 )
            image_button.image = image
            x_coordinate = 30 + (120 * idx)
            y_coordinate = 30
            if  idx >= 5:
                y_coordinate = 90
                x_coordinate = 30 + (120 * (idx - 5 ))
            image_button.place(x=x_coordinate, y=y_coordinate)
              
                
    # palette 변경
    def change_palette(self, index, camera_index):
        self.log_write(f"Changing palette CAM{camera_index} -> palette {index}")
        print(f"Changing palette for camera index: {camera_index}, palette index: {index}")
        rvalue = self.INFO[self.MAIN_INDEX]['CAMERA'].setLutID(index)
    
    
    # 팔레트 버튼 이미지 경로
    def palette_image_path(self):
        whitehot = './res/whitehot.png'
        rainbowhc = './res/rainbowhc.png'
        rainbow = './res/rainbow.png'
        lava = './res/lava.png'
        ironbow = './res/ironbow.png'
        hottest = './res/hottest.png'
        gradefire = './res/gradefire.png'
        globow = './res/globow.png'
        blackhot = './res/blackhot.png'
        arctic = './res/arctic.png'
        palette_list = [whitehot, blackhot, rainbow, rainbowhc, ironbow, lava, arctic, globow , gradefire,   hottest]
        return palette_list
    
    
    # setting 창 닫는 버튼 
    def on_toplevel_close(self, toplevel):
        self.log_write(f'CAM{self.MAIN_INDEX} Setting Window Closed')
        self.boson_disconnect()
        toplevel.destroy()
        self.toplevel_open = False
    #=======================================================================================================================================
    
    
    
    
    # 기타 함수
    #=======================================================================================================================================

    def log_write(self, massage):
        # self.logbox.insert(tk.END, massage)
        self.logbox.insert(0, massage)


    # dictionary 초기화 함수
    def Dic_Value_Init_by_Index(self,index):
        if index in self.INFO and isinstance(self.INFO[index], dict):
            inner_dict = self.INFO[index]
            print('check1 = ',inner_dict)
        for key in inner_dict.keys():
            inner_dict[key] = None


    # # 윈도우 각 index에 이미지 업데이트 함수
    def show_img(self, img, windowIndex):
        updateImg = cv2.resize(img, dsize = (320, 256))
        self.cvtimg[windowIndex] = cv2.cvtColor(updateImg, cv2.COLOR_BGR2RGBA)
        self.cvtshow[windowIndex] = Image.fromarray(self.cvtimg[windowIndex])
        self.updateImage[windowIndex] = ImageTk.PhotoImage(image=self.cvtshow[windowIndex])
        self.main_canvas.itemconfig(self.image_window[windowIndex], image = self.updateImage[windowIndex])
   

    # 딕셔너리 안에 딕셔너리의 target value list로 반환하는 함수
    def find_values_by_key(self,target):
        values = []
        for inner_dict in self.INFO.values():
            if target in inner_dict:
                values.append(inner_dict[target])
        return values     
    
    
    # 딕셔너리 key의 value들 바꿔주는 함수
    def dic_value_change(self, first_k, second_k):
        if first_k in self.INFO and second_k in self.INFO:
            self.INFO[first_k], self.INFO[second_k] = self.INFO[second_k], self.INFO[first_k]
            return True
        else:
            print("One or both keys not found.")
            return False


    def on_select(self, event):
        if event.widget == self.listbox:
            selected = self.listbox.curselection()
            if selected:  
                self.MAIN_INDEX = selected[0]
                if self.INFO[self.MAIN_INDEX]['PN'] is None:
                    self.connect()
                    self.boson_disconnect()
                    if self.INFO[self.MAIN_INDEX]['PN'][-5] == '6':
                        self.INFO[self.MAIN_INDEX]['FPS'] = 60
                        print("check fps 6")
                    elif self.INFO[self.MAIN_INDEX]['PN'][-5] == '9':
                        self.INFO[self.MAIN_INDEX]['FPS'] = 9
                        print("check fps 9")
                else:
                    print(f"Selected Index = {self.MAIN_INDEX}")
        else:
            pass

            
    #=======================================================================================================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("MDS TECH Boson SDK")
    root.geometry("900x600")  # 윈도우 크기 설정
    root.iconbitmap('./res/logo.ico')
    bg_color = "#04001f"

    main_frame = MainWindow( master=root)
    main_frame.pack(fill=tk.BOTH, expand=True)  # pack으로 변경

    thread_list = main_frame.connected_cam
    print(f"thread_list = {thread_list}")
    video_object = [None,None,None,None]
    video_thread = [None,None,None,None]

    #camera stream thread
    for idx in range(len(thread_list)):
        video_object[idx] = VideoUtilsClass(main_frame, idx, 60) # window, camera index, fps
        video_thread[idx] = threading.Thread(target=video_object[idx].image_thread, args=(idx,), daemon=True).start()
        
    root.mainloop()