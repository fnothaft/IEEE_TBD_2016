#!/usr/bin/env python3
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 2
pyKira = (944, 767)
pyKiraSDV = (10.41, 10.88)

scalaKira = (2127, 1295)
scalaKiraSDV = (5.02, 28.86)

Dis = (2280-148, 1565-139)
Dis_meta = (148, 139)
DisSDV = (342.67, 90.38)

Rep = (4918-1991, 3175-1553)
Rep_meta = (1991, 1553)
RepSDV = (70.43, 166.87)

ind = 0.1+np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars

ax = plt.subplot()
ax.set_ylim([0, 5500])
rects0 = ax.bar(ind, pyKira, width, color='blue', hatch='x', yerr=pyKiraSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))
rects1 = ax.bar(ind+width, scalaKira, width, color='orange', yerr=scalaKiraSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))
rects2 = ax.bar(ind+width*2, Dis, width, color='cyan', hatch="/")
rects3 = ax.bar(ind+width*2, Dis_meta, width, color='red', bottom=Dis, hatch="x", yerr=DisSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))

rects4 = ax.bar(ind+width*3, Rep, width, color='green', hatch="\\")
rects5 = ax.bar(ind+width*3, Rep_meta, width, color='red', bottom=Rep, hatch="x", yerr=RepSDV, ecolor='black', error_kw=dict(markersize=4, capsize=10, elinewidht=2))

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+width*2)
ax.set_xticklabels( ('256', '512'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects0[0], rects1[0], rects2[0], rects4[0], rects3[0]), ('pyKira SE', 'scalaKira SE', 'Distributed (no resilience)', 'Replicated', 'Metadata Overhead') )

plt.show()

