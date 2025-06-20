from playsound import playsound
import time

def trigger_alert(message="Breakout detected!"):
    print(f"[ALERT] {message} at {time.strftime('%H:%M:%S')}")
    try:
        playsound("assets/alert.wav")
    except Exception as e:
        print(f"Failed to play sound: {e}")
