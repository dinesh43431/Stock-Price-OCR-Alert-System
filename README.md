# Stock Price OCR Alert System

This project captures a region of your screen, uses OCR (Optical Character Recognition) to read stock prices, and triggers an alert when a target price is reached.

## Features
- Captures a specific region of the screen for price detection
- Uses Tesseract OCR to extract price from the screen
- Alerts the user when the target price is reached

## Requirements
- Python 3.8+
- Tesseract OCR (Install from https://github.com/tesseract-ocr/tesseract)
- Required Python packages (see `requirements.txt`)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/dinesh43431/Stock-Price-OCR-Alert-System.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install Tesseract OCR and update the path in `main.py` if needed:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

## Usage
1. Set your `target_price` in `main.py`.
2. Run the main script:
   ```sh
   python main.py
   ```
3. The script will monitor the screen and alert you when the price is reached.

## File Structure
- `main.py` - Main script for OCR and alert logic
- `alerts/` - Alert notification logic
- `capture/` - Screen capture logic
- `detection/` - Candlestick detection (if used)
- `utils/` - Utility functions (drawing, OCR helpers)
- `assets/` - Audio files for alerts

## Notes
- Make sure the region defined by `CROP_X`, `CROP_Y`, `WIDTH`, and `HEIGHT` in `main.py` matches the area where the price appears on your screen.
- Tesseract OCR must be installed and its path correctly set.

## License
MIT License
