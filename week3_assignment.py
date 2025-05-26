#!/usr/bin/python3
import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn import datasets
from itertools import combinations


#iris dataset
# iris_base = datasets.load_iris(as_frame=True)
# iris = iris_base.frame
# print(iris)

# plot = pyplot.hist(iris['sepal width (cm)'])
# pyplot.savefig("sepal_width_histogram.png", format = "png", dpi=300, bbox_inches="tight")
# print("Mean: ", iris['sepal width (cm)'].mean(), "\nMedian: ", iris['sepal width (cm)'].median())

# print("top 27% of sepal widths (73rd percentile): ", iris['sepal width (cm)'].quantile(q=0.73))
# #validation
# print(len(iris[iris['sepal width (cm)']>=3.3])/len(iris['sepal width (cm)']))
# print(len(iris[iris['sepal width (cm)']> 3.3])/len(iris['sepal width (cm)']))

# figure, axis = pyplot.subplots(3, 2)
# for i, combination in enumerate(combinations(['sepal length (cm)', 'sepal width (cm)',
#                                               'petal length (cm)', 'petal width (cm)'],2)):
# 	axis[i%3,i%2].scatter(iris[combination[0]],iris[combination[1]])
# 	axis[i%3,i%2].axes.set_xlabel(combination[0])
# 	axis[i%3,i%2].axes.set_ylabel(combination[1])
# figure.tight_layout()
# pyplot.savefig("multiplot.png", format = "png", dpi=300, bbox_inches="tight")


#plant growth dataset
data = { "weight": [4.17, 5.58, 5.18, 6.11, 4.50, 4.61, 5.17, 4.53, 5.33, 5.14, 4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69, 6.31, 5.12, 5.54, 5.50, 5.37, 5.29, 4.92, 6.15, 5.80, 5.26], "group": ["ctrl"] * 10 + ["trt1"] * 10 + ["trt2"] * 10}
PlantGrowth = pd.DataFrame(data)
bin_ticks = np.arange(3.3, max(PlantGrowth['weight'])+0.3, 0.3)
pyplot.hist(PlantGrowth['weight'], bins = bin_ticks)
pyplot.xticks(bin_ticks)
pyplot.savefig("weight_hist.png", format = "png", dpi=300, bbox_inches="tight")
pyplot.clf()

figure, axis = pyplot.subplots(1, 3)
for i,group in enumerate(PlantGrowth['group'].unique()):
	group_data = PlantGrowth[PlantGrowth['group'] == group]
	axis[i].boxplot(group_data['weight'])
	axis[i].axes.set_xlabel(group)
	axis[i].set_xticks([])
	axis[i].set_ylim(3.5,6.5)
figure.tight_layout()
pyplot.savefig("weight_box.png", format = "png", dpi=300, bbox_inches="tight")
cutoff = min(PlantGrowth[PlantGrowth['group']=='trt2']['weight'])
below = len(PlantGrowth[(PlantGrowth['group']=='trt1') & (PlantGrowth['weight'] < cutoff)])
total = len(PlantGrowth[PlantGrowth['group']=='trt1'])
print(below/total*100,'%', sep="")
pyplot.clf()
pyplot.style.use('fivethirtyeight')

heavy = PlantGrowth[PlantGrowth['weight']>5.5]
pyplot.bar(heavy['group'], heavy['weight'].mean())
print(heavy['weight'])
pyplot.savefig("heavy_bar.png", format = "png", dpi=300, bbox_inches="tight")
