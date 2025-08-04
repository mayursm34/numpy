import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
x=[2014,2015,2016,2017,2018,2019]
y=[18500,12700,600,14560,8550,11420]
plt.scatter(x,y,marker="1")
plt.xticks(x)
sns.set_style('darkgrid')
plt.title("dot plot")
plt.xlabel("year")
plt.ylabel("gross amount")
plt.show()

