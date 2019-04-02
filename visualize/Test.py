import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as ani

from visualize.style import PlotStyle

data = np.random.randint(1, 100, size = 20)
print(data)

# Create the figure
fig, ax = plt.subplots()


ax.clear()
PlotStyle.apply(ax)
bars = ax.bar(10)
