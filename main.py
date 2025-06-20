import pytesseract
import cv2
import time
from alerts.notifier import trigger_alert
from capture.screen_capture import get_frame

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

target_price = 1933.90 


CROP_X, CROP_Y, WIDTH, HEIGHT = 0, 152, 447, 386  

def get_price_from_screen():
    frame = get_frame()


    roi = frame[CROP_Y:CROP_Y+HEIGHT, CROP_X:CROP_X+WIDTH]

    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    
    text = pytesseract.image_to_string(
        thresh,
        config='--psm 6 -c tessedit_char_whitelist=0123456789.'
    )

    print("OCR Text:", text.strip())

    
    try:
        extracted_price = float(text.strip().replace(",", ""))
        print(f"✅ Detected Price: {extracted_price}")
        return extracted_price
    except:
        print("❌ Could not detect price.")
        return None


while True:
    price = get_price_from_screen()
    if price is not None:
        if price >= target_price:
            trigger_alert("🔔 Target Price Reached!")
            break
    time.sleep(1)
