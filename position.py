import pyautogui
import time
from pynput import mouse

def get_mouse_position():
    return pyautogui.position()

def on_click(x, y, button, pressed):
    if pressed:
        current_mouse_position = get_mouse_position()
        print(f"Mouse clicked at position: {current_mouse_position}")

def track_mouse_position():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def main():
    print("Tracking mouse position. Click to display position. Press Ctrl+C to stop.")
    track_mouse_position()

if __name__ == "__main__":
    main()