import threading
import time
import pyautogui
import walk
import gui

running = False

def start(b):
    global running
    if running:
        return
    running = True

    def loop():
        time.sleep(2)
        pyautogui.mouseDown(button='left')

        while running:
            walk.walking(b)
        pyautogui.mouseUp(button='left')

    threading.Thread(target=loop, daemon=True).start()

def stop():
    global running
    running = False


if __name__ == "__main__":
    gui.run(start, stop)