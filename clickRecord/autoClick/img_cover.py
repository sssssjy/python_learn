import cv2 as cv
import os
import numpy as np

curPath = os.path.abspath('.')
bgImgPath = os.path.join(curPath, 'clickRecord', 'autoClick', 'bg.png')
start_img_path = os.path.join(curPath, 'clickRecord', 'autoClick', 'start.png')

# bgImg = cv.imread(bgImgPath)
# # 灰度
# bgImgGray = cv.cvtColor(bgImg, cv.COLOR_BGR2GRAY)
# # 高斯模糊化 去除噪点
# # bgImgBlur = cv.GaussianBlur(bgImgGray, (3, 3), cv.BORDER_DEFAULT)

# cv.imshow("bgImgGray", bgImgGray)
# # cv.imshow("bgImgBlur", bgImgBlur)

# # 一直等待 否则图片展示不出来
# cv.waitKey(0)

# import cv2
 
# 读取图像
image = cv.imread(bgImgPath)
# image = cv.imread(start_img_path)
cv.imshow("img", image)
 
gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 寻找轮廓
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
 
# 显示图像
# 绘制绿色轮廓
cv.drawContours(image, contours, -1, (0,255,0), 3)
cv.imshow("draw", image)

cv.waitKey(0)
cv.destroyAllWindows()