import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy.random import normal
import unicodecsv as csv

def read_csv(filename):
	with open(filename, 'rb') as f:
		reader = csv.DictReader(f)
		return list(reader)

product_data = read_csv('C:/Users/dano/Desktop/ProductSuccessAnalysis/UpdatedProductSuccess.csv')
feature_array = ['Connectivity','Advanced','Satisfies Need','Well-Priced','Well-Marketed','Usability','Convenient','Design','Necessity','Superiority','Personalization']
fig = plt.figure()
ax = fig.add_subplot(111)

def factor_processed(array,featureName):
	feature_array = []
	for row in array:
		feature_array.append(row[featureName])
	return feature_array
"""
connectivity = factor_processed(product_data,"Connectivity")
advanced = factor_processed(product_data,"Advanced")
satisfies_need = factor_processed(product_data,"Satisfies Need")
well_priced = factor_processed(product_data,"Well-Priced")
well_marketed = factor_processed(product_data,"Well-Marketed")
usability = factor_processed(product_data,"Usability")
convenient = factor_processed(product_data,"Convenient")
design = factor_processed(product_data,"Design")
necessity = factor_processed(product_data,"Necessity")
superiority = factor_processed(product_data,"Superiority")
personalization = factor_processed(product_data,"Personalization")
"""
product_array = []
for row in product_data:
	product_array.append(row['Product'])

ind = np.arange(18)
width = 0.1

#connct_bar = ax.bar(ind,  connectivity,product_array, width, color='black')
"""
for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]): second one is where it is on Y axis
    xs = np.arange(20)
    ys = np.random.rand(20)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, connectivity, zdir='y', color=cs, alpha=0.8)
"""
it = 1
for feature in feature_array:

	for colour in ['r','g','b','y']:
		xs = np.arange(20)
		cs = [colour] * len(xs)
		cs[0] = 'c'

	featureProcessed = factor_processed(product_data,feature)
	ax.bar(ind+(width*it),featureProcessed,width,color=cs)
	it += 1
"""
adv_bar = ax.bar(ind+width, advanced, width, color='grey')
need_bar = ax.bar(ind+(width * 2), satisfies_need, width, color='red')
price_bar = ax.bar(ind+(width * 3), well_priced, width, color='green')
marketed_bar = ax.bar(ind+(width * 4), well_marketed, width, color='blue')
usability_bar = ax.bar(ind+(width * 5), usability, width, color='yellow')
convenient_bar = ax.bar(ind+(width * 6), convenient, width, color='pink')
design_bar = ax.bar(ind+(width * 7), design, width, color='cyan')
necessity_bar = ax.bar(ind+(width * 8), necessity, width, color='orange')
super_bar = ax.bar(ind+(width * 9), superiority, width, color='turquoise')
person_bar = ax.bar(ind+(width * 10), personalization, width, color='purple')
"""

ax.set_xlim(-width,len(ind)+(width * 10))
ax.set_ylim(0,20)
ax.set_ylabel("Frequency")
ax.set_title("Patterns of product success")

ax.set_xticks(ind+width)

xtickNames = ax.set_xticklabels(product_array)

for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(10)

plt.setp(xtickNames,fontsize=10)

#ax.legend( (ps_bar[0]), ('Connectivity') )

plt.show()