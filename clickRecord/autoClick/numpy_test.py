#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import os
import numpy as np
import matplotlib.gridspec as gridspec

txtList = [
    'test2023_09_29_15_39_45.txt', 
    'test2023_09_29_16_22_22.txt',
    'test2023_09_29_17_07_23.txt', 
    'test2023_09_29_18_00_07.txt', 
    'test2023_09_29_22_52_31.txt'
]

minX = 828
minY = 451
maxX = 940
maxY = 570

midX = (minX + maxX) / 2
midY = (minY + maxY) / 2

def init_bg_img(ax):
    curPath = os.path.abspath('.')
    imgPath = os.path.join(curPath, 'clickRecord', 'autoClick', 'bg.png')

    with cbook.get_sample_data(imgPath) as image_file:
        image = plt.imread(image_file)
    ax.imshow(image)

    ax.set_ylim(589, 0)
    ax.set_xlim(0, 964)

def getTemplateDotPosition(txtList):
    curPath = os.path.abspath('.')
    x = []
    y = []
    positions = []
    for txt in txtList:
        txtName = os.path.join(curPath, 'clickRecord', txt)
        with open(txtName, 'r', encoding='utf8') as file:
            for line in file.readlines():
                pos = line.split(',')
                x.append(int(pos[0]))
                y.append(int(pos[1]))
                positions.append([int(pos[0]), int(pos[1])])
    return (x, y, positions)

def showTemplateDots(ax, txtList):
    x, y, positions = getTemplateDotPosition(txtList)
    sizes = np.random.uniform(1, 1, len(x))
    ax.set_ylim(589, 0)
    ax.set_xlim(0, 964)
    ax.scatter(x, y, sizes=sizes)

# 根据均值、标准差,求指定范围的正态分布概率值
def normfun(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))


def randomStartClick(ax):
    count = 1000

    # 随机生成，整体正态分布
    # result = np.random.randint(0, 100, size=100) # 最小值,最大值,数量
    randomX = np.random.normal(midX, 15, count)  # 均值,标准差,数量
    randomY = np.random.normal(midY, 15, count)  # 均值,标准差,数量
    sizes = np.random.uniform(1, 1, len(randomX))
    ax.set_ylim(589, 0)
    ax.set_xlim(0, 964)
    colors = np.random.uniform(15, 15, count)
    ax.scatter(randomX, randomY, sizes=sizes, c=colors)

def randomEndClick(ax):
    count = 500

    x = midX - 20
    y = midY - 65

    # 随机生成，整体正态分布
    # result = np.random.randint(0, 100, size=100) # 最小值,最大值,数量
    randomX = np.random.normal(x, 30, count)  # 均值,标准差,数量
    randomY = np.random.normal(y, 30, count)  # 均值,标准差,数量
    sizes = np.random.uniform(1, 1, len(randomX))
    colors = np.random.uniform(15, 15, count)
    ax.scatter(randomX, randomY, sizes=sizes, c=colors)

def init():
    plt.figure()
    ax = plt.subplot()
    # init_bg_img(ax)
    showTemplateDots(ax, txtList)
    plt.figure()
    ax = plt.subplot()
    randomStartClick(ax)
    randomEndClick(ax)

    plt.show()

init()
