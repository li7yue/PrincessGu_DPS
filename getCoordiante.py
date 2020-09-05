import os,time
import pyautogui as pag
try:
    while True:
            print("Press Ctrl-C to end")
            # 返回鼠标的坐标
            x,y = pag.position()
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            # 打印坐标
            print (posStr)
            time.sleep(0.2)
            # 清除屏幕
            os.system('cls')
except KeyboardInterrupt:
    print ('end....')

# dmg       504 195 550 208
# time      705 170 731 182