#capture.py
import cv2
import numpy as np
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#16bit Grayscale 변환
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
#자동 rgb변환 비활성화
cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)

start_x = 200
start_y = 200
end_x = 350
end_y = 350

def pixel_to_temp(image):
    temp = (image/100) - 273.15
    max_temp = f"max_temp = {(round(np.max(temp), 2))}"
    min_temp = f"min_temp = {(round(np.min(temp), 2))}"
    avg_temp = f"avg_temp = {(round(np.mean(temp), 2))}"
    
    return max_temp, min_temp, avg_temp

def bit_change(image):
    min_val = np.min(image)
    max_val = np.max(image)
    show_img = (image - min_val) / (max_val - min_val)
    img_8bit = (show_img * 255).astype(np.uint8)
    rgb_img = cv2.cvtColor(img_8bit, cv2.COLOR_GRAY2RGB)
    return rgb_img

while True:
    stream_ret, frame = cap.read()
    frame = np.array(frame)
    rgb_img = bit_change(frame)
    
    temp_image = frame.copy()

    res = temp_image[start_y : end_y, start_x : end_x] #start_y, end_y, startx
    max_temp, min_temp, avg_temp = pixel_to_temp(res)
    if stream_ret:
        cv2.rectangle(rgb_img, (start_x, start_y), (end_x, end_y), (0, 0, 255) , 3)
        cv2.putText(rgb_img, max_temp,  (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0, 255, 0), 1)
        cv2.putText(rgb_img, min_temp,  (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0, 255, 0), 1)
        cv2.putText(rgb_img, avg_temp,  (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0, 255, 0), 1)
        output = cv2.resize(rgb_img, (800,600))
        cv2.imshow("pixel_to_temp", rgb_img)
    if cv2.waitKey(1) == ord('q'):
        break;
cv2.destroyAllWindows()
