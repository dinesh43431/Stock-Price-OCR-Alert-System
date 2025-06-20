import pytesseract
import cv2
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_price_from_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(gray, config='--psm 7 -c tessedit_char_whitelist=0123456789.')
    match = re.search(r'\d+\.\d+', text)

    if match:
        return float(match.group())
    return None
