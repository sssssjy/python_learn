import pyautogui
# 屏幕大小
screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

# 当前鼠标坐标
print(pyautogui.position())

# x, y 是否在屏幕上
x, y = 1099, 2388
print(pyautogui.onScreen(x, y))

# 保护措施
# 增加延迟
pyautogui.PAUSE = 1

# 防止程序死机
# 当光标移到左上角时 抛出异常
pyautogui.FAILSAFE = True

# 用x秒时间将鼠标移动到指定位置
sec = 1.34
pyautogui.moveTo(200, 406, duration=sec)

# 用x秒时间将鼠标相对移动y距离
xOffset, yOffset = 403, -62
pyautogui.moveRel(xOffset, yOffset, duration=sec)

#  开始很慢，不断加速
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
#  开始很快，不断减速
pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
#  开始和结束都快，中间比较慢
pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
#  一步一徘徊前进
pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)
#  徘徊幅度更大，甚至超过起点和终点
pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)

# 所有点击函数
moveToX, moveToY = 828, 995
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

# 鼠标滚轮函数
# clicks 代表滚动格数 正代表向下，负代表向上
pyautogui.scroll(clicks=-2, x=moveToX, y=moveToY)

# 点击可分为点下松开
pyautogui.mouseDown(x=moveToX, y=moveToY)
pyautogui.mouseUp(x=moveToX, y=moveToY)

# 鼠标拖拽
#  按住鼠标左键，把鼠标拖拽到(100, 200)位置
pyautogui.dragTo(100, 200, button='left')
#  按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
pyautogui.dragTo(300, 400, 2, button='left')
#  按住鼠标右键，用2秒钟把鼠标拖拽到(30,0)位置
pyautogui.dragTo(30, 0, 2, button='right')

# 键盘函数
# 输入间隔
key_sec = 0.15
pyautogui.typewrite('hello world', interval=key_sec)

# 热键
pyautogui.hotkey('ctrl', 'c')
