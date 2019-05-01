import matplotlib.animation as ani
from visualize.style import PlotStyle
import matplotlib.pyplot as plt
import random
import math
import time
import numpy as np
u_input = int(input())
#arr = [[random.randint(1,50) for k in range(2)]for l in range(int(input()))]

x, y = [random.randint(1,50) for i in range(u_input)], [random.randint(1,50) for j in range(u_input)]


xy = []
for k in range(u_input):
    xy.append([x[k], y[k]])

print(xy)

routes = []
dist = [[]]

possible_ham_cir = math.factorial(u_input)
possible_edges = int(u_input + ((u_input*(u_input - 3))/2))
print("edges ammount: " + str(possible_edges))
edges = []
#print(possible_ham_cir)
used_points = []
print(possible_edges)
for u in range(len(xy)):
    placehold = []
    for t in range(len(xy)):
        if t == u:
            continue
        placehold.append(round(math.sqrt(((xy[t][0] - xy[u][0]) ** 2) + (xy[t][1] - xy[u][1]) ** 2), 2))

    edges.append(placehold)

print("edges: " + str(edges))

plt.axis(xmin = 0, ymin = 0, xmax = 50, ymax = 50)
#print(x,y)
plt.scatter(x,y)
plt.show()

