import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
print(x, y)

sizes = np.random.uniform(1, 1, len(x))
colors = np.random.uniform(15, 80, len(x))

plt.scatter(x, y, s=sizes, c=colors)
plt.show()
