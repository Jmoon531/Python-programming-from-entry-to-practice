#!usr/bin/env python

import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()
points_number = list(range(rw.num_points))
plt.figure(figsize=(20, 10))
plt.scatter(rw.x_values, rw.y_values, c=points_number, cmap=plt.cm.Blues, edgecolors='none', s=1)
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
