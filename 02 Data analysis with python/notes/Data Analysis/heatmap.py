import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
correlacion = df.corr()

fig, ax = plt.subplots()
im = ax.pcolor(correlacion, cmap='jet')

#label names
row_labels = correlacion.columns
col_labels = correlacion.index

#move ticks and labels to the center
ax.set_xticks(np.arange(correlacion.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(correlacion.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=45, ha='right', va='top')
plt.title("Variables Correlation")

fig.colorbar(im)
plt.show()
