import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from numpy.random import normal

data = np.array([1,2,2,3,4])

fig = plt.figure()
ax = fig.add_subplot(111)

N = 5
menMeans = [18, 35, 30, 35, 27]
menStd = [2, 3, 4, 1, 2]
womenMeans = []
womenStd = []

ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, menMeans, width, color='black',yerr=menStd)

ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,45)
ax.set_ylabel("Frequency")
ax.set_title("Patterns of product success")

xTickMarks = ['Group' + str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames,rotation=45,fontsize=10)

plt.show()