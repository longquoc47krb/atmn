import pyautogui
import time
import keyboard

POSITION_TAX_CODE = (65, 153)
POSITION_BROWSER = (147, 585)
POSITION_DATE = (453, 157)
POSITION_NOTE = (343, 269)
POSITION_AMOUNT = (455, 378)
POSITION_CONFIRM_BTN = (474, 431)

def delay(times):
    time.sleep(0.85*times)

def move_and_click(position, double_click=False):
    pyautogui.moveTo(position)
    if double_click:
        pyautogui.doubleClick()
    else:
        pyautogui.click()
def press_hotkey(*keys):
    pyautogui.hotkey(*keys)
    delay(0.12)
def press_key(key, times=1):
    for _ in range(times):
        pyautogui.press(key)
    delay(0.12)
def type_text(text):
    pyautogui.typewrite(text)
    delay(0.12)
def copy():
    press_hotkey("ctrl", "c")
    delay(0.12)
def paste():
    press_hotkey("ctrl", "v")
def change_window():
    press_hotkey("alt", "tab")
    delay(0.15)
def main():
    try:
        delay(7)
        for _ in range(310):
            if keyboard.is_pressed('ctrl+esc'):
                print("Stopping script...")
                break
            copy()
            change_window()
            move_and_click(POSITION_BROWSER)
            press_hotkey("ctrl", "shift", "c")
            delay(1.5)
            press_hotkey("ctrl", "a")
            paste()
            delay(1.5)
            press_hotkey("enter")
            change_window()
            press_key("left", 5)
            copy()
            change_window()
            move_and_click(POSITION_DATE, True)
            press_hotkey("ctrl", "a")
            paste()
            change_window()
            press_key("right", 1)
            press_hotkey("ctrl", "b")
            copy()
            change_window()
            move_and_click(POSITION_AMOUNT, True)
            paste()
            change_window()
            press_key("right", 5)
            copy()
            change_window()
            move_and_click(POSITION_NOTE, True)
            press_hotkey("ctrl", "a")
            press_hotkey("delete")
            paste()
            press_hotkey("ctrl", "s")
            delay(1.5)
            move_and_click(POSITION_CONFIRM_BTN)
            delay(2)
            change_window()
            press_key("left", 1)
            press_key("down", 1)
    except KeyboardInterrupt:
        print("Script interrupted.")

if __name__ == "__main__":
    main()
