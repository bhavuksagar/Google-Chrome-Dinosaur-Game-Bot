import pyautogui
from PIL import ImageGrab,Image
import time
import webbrowser


def detect(data):
    for i in range(185,340):
        for j in range(399,478):
            if data[i, j] > 200:
                pyautogui.keyDown('down')
                return

    for i in range(185,340):
        for j in range(457, 520):
            if data[i, j] > 150:
                pyautogui.keyDown('up')
                return
    return

if __name__ == '__main__':
    print("game will start in 3 sec")
    webbrowser.open("chrome://dino")
    time.sleep(2)
    pyautogui.keyDown('up')
    while True:
        image= ImageGrab.grab().convert('L')
        data= image.load()
        detect(data)
