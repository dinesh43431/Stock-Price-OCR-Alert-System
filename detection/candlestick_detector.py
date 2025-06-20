import cv2
import numpy as np
from config import MIN_CANDLE_AREA

def detect_candlesticks(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    green_mask = cv2.inRange(hsv, (50, 100, 100), (70, 255, 255))
    red_mask = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))

    green_candles = _find_candle_contours(green_mask, frame, (0, 255, 0))
    red_candles = _find_candle_contours(red_mask, frame, (0, 0, 255))

    return green_candles + red_candles

def _find_candle_contours(mask, frame, color):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    candles = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > MIN_CANDLE_AREA:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            candles.append((x, y, w, h))
    return candles