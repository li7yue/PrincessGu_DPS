import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import os

def recogPattern():
    data = list()
    x_axis = list()
    count = 0
    while count <= 92:
        text_data = pytesseract.image_to_string(Image.open(os.path.dirname(os.path.abspath(__file__)) + '\\pngInvert\\' + str(count) + '.png'))
        count += 1
        try:
            print(text_data)
            if int(text_data) <= 775000 and int(text_data) > 360000:
                data.append(int(text_data))
                x_axis.append(count)
            else:
                print('dataNotGood')
        except ValueError:
            pass
    return data, x_axis

def plotData(x, y):
    fig = plt.figure()
    plt.scatter(x, y, color='r', marker='+')
    plt.show()

if __name__ == "__main__":
    dmg, time = recogPattern()
    plotData(time, dmg)