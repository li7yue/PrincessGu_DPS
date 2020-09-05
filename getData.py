import time
from PIL import ImageGrab
import os

def screenshot(count):
    im = ImageGrab.grab((504, 195, 550, 208))
    im_time = ImageGrab.grab((705, 170, 731, 182))
    im.save(os.path.dirname(os.path.abspath(__file__)) + '\\png\\' + str(count) + '.png')
    im_time.save(os.path.dirname(os.path.abspath(__file__)) + '\\pngTime\\' + str(count) + '.png')

if __name__ == "__main__":
    num = 0
    while True:
        print('Prt Scn')
        print(num)
        screenshot(num)
        num += 1
        time.sleep(1)