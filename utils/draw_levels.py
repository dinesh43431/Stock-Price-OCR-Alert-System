import cv2
from config import SUPPORT_Y, RESISTANCE_Y

def draw_levels(frame):
    cv2.line(frame, (0, SUPPORT_Y), (frame.shape[1], SUPPORT_Y), (255, 0, 0), 2)
    cv2.line(frame, (0, RESISTANCE_Y), (frame.shape[1], RESISTANCE_Y), (0, 0, 255), 2)