import os
from PIL import Image
import numpy as np
 
def invert(imgPath, savePath):
    files = os.listdir(imgPath)
    files.sort()
    print('start inverting:',imgPath)
    for file in files:
        fileType = os.path.splitext(file)
        if fileType[1] == '.png':
            # 打开图片
            new_png = Image.open(imgPath+'/'+file)
            # 图像转矩阵并反色
            matrix = 255-np.asarray(new_png)
            # 矩阵转图像
            new_png = Image.fromarray(matrix)
            # 保存图片
            new_png.save(savePath+'/'+file)
    print('invert complete')
 
if __name__ == '__main__':
    # 待处理图片地址
    dataPath = os.path.dirname(os.path.abspath(__file__)) + '\\png\\'
    # 保存图片的地址
    savePath = os.path.dirname(os.path.abspath(__file__)) + '\\pngInvert\\'
    invert(dataPath, savePath)