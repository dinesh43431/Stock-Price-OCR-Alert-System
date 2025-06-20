import pyautogui
import time

print("Move your mouse to TOP-LEFT corner of the price box...")
time.sleep(5)
x1, y1 = pyautogui.position()
print(f"Top-left corner: ({x1}, {y1})")

print("Now move to BOTTOM-RIGHT corner of the price box...")
time.sleep(5)
x2, y2 = pyautogui.position()
print(f"Bottom-right corner: ({x2}, {y2})")

width = x2 - x1
height = y2 - y1
print(f"Region: x={x1}, y={y1}, width={width}, height={height}")
