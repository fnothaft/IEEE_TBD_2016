#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4
scalaKira = (4539, 2322, 1236, 819)
pyKira = (855, 537, 378, 386)
C = (612, 514, 408, 371)
scalaSlowdown=(7.42, 4.52, 3.03, 2.21)
pySlowdown=(1.4, 1.04, 0.925, 1.04)

ind = 0.125+np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

ax = plt.gca()
ax.grid(True)
plt.yticks(size='large')
ax_c = ax.twinx()
ax_c.set_ylim([0, 9])
rects1 = ax.bar(ind, pyKira, width, color='blue', hatch="x")
rects2 = ax.bar(ind+width, scalaKira, width, color='orange')
rects3 = ax.bar(ind+width*2, C, width, color='red', hatch="/")
rects4 = ax_c.plot(ind+width*0.5, pySlowdown, linestyle='--', marker='o', markersize=8.0, mew=2.0, c='blue', linewidth=4.0)
rects5 = ax_c.plot(ind+width*1.5, scalaSlowdown, linestyle='-', marker='D', markersize=8.0, mew=2.0, c='orange', linewidth=4.0)





plt.yticks(size='large')
# add some text for labels, title and axes ticks
ax.set_xlabel('Scale', size='x-large')
ax.set_ylabel('Time-to-solution (seconds in log scale)', size='x-large')
ax.set_yscale("log")
ax_c.set_ylabel('Relative Performance Compared to C', size='x-large')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1 core', '2 cores', '4 cores', '8 cores'), size='x-large') 

ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Kira-SE-v2', 'Kira-SE-v1', 'C', 'Kira-SE-v2 Relative', 'Kira-SE-v1 Relative') )

plt.show()

