import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)

df_agrupado2 = df[["make", "price"]]
grupo_test2 = df_agrupado2.groupby(["make"], as_index = False).mean()
grupo_test2 = grupo_test2.sort_values("price")

make = grupo_test2['make']
price = grupo_test2['price']
ypos = np.arange(len(make))

# ha = horizontalmente alineado, va = verticalmente alineado
# plt.xticks(ypos, make, rotation = 45, ha = "right")
plt.xticks(ypos, make, rotation = 45, ha = "right", va = "top")
plt.xlabel("make")
plt.ylabel("price")
plt.title("AVG price")
plt.bar(ypos, price, color = "#8a2be2", zorder = 2)
plt.ylim(0,35000)
plt.grid(color = "#cdd4e4", linestyle = "dashed", zorder = 0)
plt.show()
