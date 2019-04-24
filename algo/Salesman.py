import matplotlib.animation as ani
from visualize.style import PlotStyle
import matplotlib.pyplot as plt
import random
import time
import numpy as np
u_input = int(input())
#arr = [[random.randint(1,50) for i in range(2)]for j in range(int(input()))]

x, y = [random.randint(1,50) for i in range(u_input)], [random.randint(1,50) for i in range(u_input)]

plt.axis(xmin = 0, ymin = 0, xmax = 50, ymax = 50)
print(x,y)
plt.scatter(x,y)
plt.show()

