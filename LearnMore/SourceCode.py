import time
import threading
import pyautogui
import keyboard
import random

stop_program = False

# Disable pyautogui failsafe
pyautogui.FAILSAFE = False

def monitor_stop_key():
    """Monitors for CTRL + CapsLock to stop the program."""
    global stop_program
    keyboard.wait('ctrl+caps lock')
    stop_program = True

def press_F13_key():
    """Press 'F13' every 30–90 seconds until stopped."""
    while not stop_program:
        pyautogui.press('F13')
        # Random wait between 30–90 seconds
        wait_time = random.randint(30, 90)
        for _ in range(wait_time):
            if stop_program:
                break
            time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=monitor_stop_key, daemon=True).start()
    press_F13_key()
