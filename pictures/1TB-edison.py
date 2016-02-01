#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 1
pyKira = (767)
pyKiraSDV = (10.88)

scalaKira = (1295)
scalaKiraSDV = (28.86)

Edison = (1389-201)
Edison_meta = (201)
EdisonSDV = (520.53)

ind = 0.35+np.arange(N)  # the x locations for the groups
width = 0.1       # the width of the bars

ax = plt.subplot()
#ax.set_ylim([0, 2500])
rects1 = ax.bar(ind, pyKira, width, color='blue', hatch='x', yerr=pyKiraSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))
rects2 = ax.bar(ind+width, scalaKira, width, color='orange', yerr=scalaKiraSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))

rects3 = ax.bar(ind+width*2, Edison, width, color='cyan', hatch="\\")
rects4 = ax.bar(ind+width*2, Edison_meta, width, color='red', bottom=Edison, hatch="x", yerr=EdisonSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+width*1.5)
ax.set_xticklabels( ('512', ''), size='x-large') 
plt.yticks(size='large')
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('pyKira SE', 'scalaKira SE', 'Edison', 'Metadata Overhead'),loc='best')

plt.show()

