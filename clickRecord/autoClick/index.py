import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import os
import numpy as np


def init_bg_img():
    curPath = os.path.abspath('.')
    imgPath = os.path.join(curPath, 'clickRecord', 'autoClick', 'bg.png')

    with cbook.get_sample_data(imgPath) as image_file:
        image = plt.imread(image_file)
    fig, ax = plt.subplots()
    ax.imshow(image)

    ax.set_ylim(589, 0)


# 根据均值、标准差,求指定范围的正态分布概率值
def normfun(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))


row = 100  # 行
cols = 100  # 列

# 随机生成，整体正态分布
# result = np.random.randint(0, 100, size=100) # 最小值,最大值,数量
result = np.random.normal(60, 20, (row, cols))  # 均值,标准差,数量
print(result)

init_bg_img()
# plt.show()
