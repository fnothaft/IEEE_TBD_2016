#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 5
HDD = (290, 173, 100, 72, 47)
HDD_SDV = (6.2, 4.3, 0.7, 0.9, 2.6)
SSD = (147, 89, 59, 36, 30)
SSD_SDV = (1.1, 1.4, 1.3, 2, 1.8)

ind = 0.15+np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

ax = plt.subplot()
#ax.set_yscale("log", nonposx='clip')
rects1 = ax.bar(ind, SSD, width, color='blue', yerr=SSD_SDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))
rects2 = ax.bar(ind+width, HDD, width, color='orange', hatch="x", yerr=HDD_SDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds in log scale)', size='x-large')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('32', '64', '128', '256', '512'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0]), ('Kira-SE-v2 on SDD', 'Kira-SE-v2 on HDD') )

plt.show()

