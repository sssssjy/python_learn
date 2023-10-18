import pyautogui
from pynput.keyboard import Key, Listener
import os
from pyautogui import ImageNotFoundException

# locateAllOnScreen
def getStartImgPosition(callback):
    curPath = os.path.abspath('.')
    imgPath = os.path.join(curPath, 'clickRecord', 'autoClick', 'start.png')
    try:
        loc = pyautogui.locateOnScreen(imgPath, confidence=0.8, grayscale=True)
        if loc == None:
            print('start button is not found, please try again')
        else:
            callback(loc)
    except ImageNotFoundException:
        print('start button is not found, please try again')
        return False

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def init_on_release(callback):
    def on_release(key):
        print('{0} released'.format(
            key))
        if key == Key.enter:
            getStartImgPosition(callback)
        if key == Key.esc:
            # Stop listener
            return False
    
    return on_release


def initWatch(callback):
    on_release = init_on_release(callback)
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()
