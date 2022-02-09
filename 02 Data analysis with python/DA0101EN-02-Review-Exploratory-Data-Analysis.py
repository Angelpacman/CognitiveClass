import pandas as pd
import numpy as np

path = 'automobileEDA.csv'
df = pd.read_csv(path)
df.head()

import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

agrupados_corr = df.corr()
agrupados_corr

fig, ax = plt.subplots()
im = ax.pcolor(agrupados_corr, cmap='gnuplot2')

#label names
row_labels = agrupados_corr.columns
col_labels = agrupados_corr.index

#move ticks and labels to the center
ax.set_xticks(np.arange(agrupados_corr.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(agrupados_corr.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=45, ha="right")

fig.colorbar(im)
plt.show()
