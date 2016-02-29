import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from numpy.random import normal
import unicodecsv as csv

def read_csv(filename):
	with open(filename, 'rb') as f:
		reader = csv.DictReader(f)
		return list(reader)

product_data = read_csv('C:/Users/dano/Desktop/ProductSuccessAnalysis/UpdatedProductSuccess.csv')

fig = plt.figure()
ax = fig.add_subplot(111)

def factor_processed(array,featureName):
	feature_array = []
	for row in array:
		feature_array.append(row[featureName])
	return feature_array

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

ind = np.arange(18)
width = 0.1

connct_bar = ax.bar(ind, connectivity, width, color='black')
adv_bar = ax.bar(ind+width, advanced, width, color='grey')
need_bar = ax.bar(ind+(width * 2), advanced, width, color='red')
price_bar = ax.bar(ind+(width * 3), advanced, width, color='green')
marketed_bar = ax.bar(ind+(width * 4), advanced, width, color='blue')
usability_bar = ax.bar(ind+(width * 5), advanced, width, color='yellow')
convenient_bar = ax.bar(ind+(width * 6), advanced, width, color='pink')
design_bar = ax.bar(ind+(width * 7), advanced, width, color='cyan')
necessity_bar = ax.bar(ind+(width * 8), advanced, width, color='orange')
super_bar = ax.bar(ind+(width * 9), advanced, width, color='turquoise')
person_bar = ax.bar(ind+(width * 10), advanced, width, color='purple')


ax.set_xlim(-width,len(ind)+(width * 10))
ax.set_ylim(0,20)
ax.set_ylabel("Frequency")
ax.set_title("Patterns of product success")

xTickMarks = []
for row in product_data:
	xTickMarks.append(row['Product'])

ax.set_xticks(ind+width)

xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames,fontsize=10)

#ax.legend( (ps_bar[0]), ('Connectivity') )

plt.show()