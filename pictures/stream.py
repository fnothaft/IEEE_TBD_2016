#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

x8 = np.multiply(np.arange(1,12), 8)
y8 = (18.28, 8.75, 8.38, 6.72, 7.44, 7.34, 7.10, 7.29, 6.79, 7.69, 6.70)

x4 = np.multiply(np.arange(1, 23), 4)
y4 = (13.36, 4.61, 4.08, 4.30, 4.15, 3.94, 4.49, 3.85, 3.97, 3.75, 3.59,
  3.80, 3.63, 3.56, 4.30, 4.02, 3.55, 3.64, 3.60, 4.59, 3.76, 3.56)

x2 = np.multiply(np.arange(1, 45), 2)
y2 = (12.31, 3.31, 2.92, 3.13, 2.66, 2.60, 2.58, 2.62, 2.80, 2.44, 2.26,
  2.29, 2.34, 2.33, 2.44, 2.36, 2.53, 2.35, 2.43, 2.54, 2.27, 2.19, 
  3.04, 2.38, 2.28, 2.83, 2.29, 2.26, 2.25, 2.40, 2.50, 2.32, 3.07, 
  2.41, 2.40, 2.54, 2.60, 2.14, 2.26, 3.00, 2.19, 2.27, 2.34, 1.56)

x1 = np.arange(1, 89)
y1 = (11.83, 2.60, 2.39, 2.22, 2.15, 2.80, 2.34, 1.99, 1.85, 1.73, 1.87,
  1.98, 2.07, 1.63, 1.64, 1.77, 2.05, 1.83, 1.81, 2.13, 2.07, 1.60,
  1.75, 1.59, 2.26, 1.54, 1.46, 1.54, 1.93, 1.49, 1.65, 1.80, 1.78,
  1.53, 2.30, 2.27, 1.56, 1.88, 1.62, 1.66, 2.04, 1.77, 1.80, 1.70,
  1.60, 1.60, 1.65, 2.03, 1.43, 1.44, 1.41, 1.68, 1.53, 1.78, 2.06,
  1.89, 1.79, 1.61, 1.90, 1.68, 1.58, 2.04, 1.48, 1.68, 2.28, 1.53,
  1.52, 1.80, 2.35, 1.64, 1.63, 1.55, 1.62, 1.96, 1.95, 1.65, 1.60,
  1.85, 2.53, 1.55, 1.60, 1.60, 1.62, 1.69, 1.91, 1.58, 1.46, 0.72)

fig, ax = plt.subplots()
ax.set_xlim(0, 90)
ax.set_ylim(0, 20)
ax.set_xlabel('Data Arrival Sequence (780 MB per Arrival)', size='x-large')
ax.set_ylabel('Overall Delay (seconds)', size='x-large')
plt.xticks(size='large')
plt.yticks(size='large')
with plt.style.context('fivethirtyeight'):
  ax.plot(x8, y8, 'o-', ms='10', c='blue')
  ax.plot(x4, y4, '^-', ms='10', c='yellow')
  ax.plot(x2, y2, 's-', ms='5', c='green')
  ax.plot(x1, y1, c='red')
ax.legend(('8 arrival interval', '4 arrival interval', '2 arrival interval', '1 arrival interval') )
plt.show()
