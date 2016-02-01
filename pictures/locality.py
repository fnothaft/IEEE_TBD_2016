#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 6
Kira = (100, 69, 73, 80, 82, 82)
KiraSDV = (0, 0.02, 1.06, 0.55, 0.38, 0.19)
C = (100, 50, 25, 12.5, 6.3, 3.2)

ind = 0.15+np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

ax = plt.subplot()
rects1 = ax.bar(ind, Kira, width, color='blue', hatch="x", yerr=np.multiply(KiraSDV, 1), ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))
#rects1 = ax.bar(ind, Kira, width, yerr=KiraSDV, color='b', ecolor='black', error_kw=dict(elinewidth=4, capsize=4, markersize=10))
rects2 = ax.bar(ind+width, C, width, color='red', hatch="/")
ax.set_ylim([0, 100])
ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Locality hit ratio (percentage)', size='x-large')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('8', '32', '64', '128', '256', '512'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0]), ('pyKira', 'C Estimated') )

plt.show()

