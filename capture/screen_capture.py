import mss
import numpy as np
import cv2

def get_frame():
    with mss.mss() as sct:
        
        screen_width = sct.monitors[1]['width']
        screen_height = sct.monitors[1]['height']
        
        left = 0
        top = screen_height // 3
        width = screen_width // 2
        height = screen_height // 4
        
        monitor = {"top": top, "left": left, "width": width, "height": height}
        sct_img = sct.grab(monitor)
        
        img = np.array(sct_img)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
