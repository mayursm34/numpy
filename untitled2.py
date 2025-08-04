import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
y1=np.random.normal(-2,2,1000)
y2=np.random.normal(-2,2,1000)
sns.histplot(y1)
sns.histplot(y2)
plt.title("histogram")
plt.show()
