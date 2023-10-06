from pynput import mouse
import os
import time

clickList = []


def watchClick(x, y):
    print(x, y)
    clickList.append({
        'x': x,
        'y': y,
        'time': int(round(time.time() * 1000))
    })


def handleResult():
    curPath = os.path.abspath('.')
    fileName = os.path.join(curPath, 'clickRecord', 'test%s.txt' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
    with open(fileName, 'w', encoding='utf8') as file:
        for position in clickList:
            file.write('%s,%s,%s\n' % (position['x'], position['y'], position['time']))


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        watchClick(x, y)
    if button == mouse.Button.middle:
        raise Exception(button)


# Collect events until released
with mouse.Listener(
        on_click=on_click) as listener:
    try:
        listener.join()
    except Exception:
        print('click end')
        handleResult()
