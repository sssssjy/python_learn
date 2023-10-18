from recognize_img import initWatch
from position import Position
import pyautogui

from random_position import create_random_start_position

pos = Position()

def click_start_btn(start_pos):
    random_start_pos = create_random_start_position(start_pos)
    print(random_start_pos, 'random_start_pos', start_pos)
    pyautogui.moveTo(start_pos['center_position'])
    # pyautogui.moveTo(random_start_pos)
    pyautogui.click()
    print('111')

def initStart(loc):
    # Box(left=2114, top=988, width=186, height=176)
    pos.init_start_position(loc)
    start_pos = pos.get_start_position()
    click_start_btn(start_pos=start_pos)

initWatch(callback=initStart)
