# Histograms
This is a way of representing frequency distribution of a variable

###### Pasos para hacer histogramas:
- partir el eje horizontal en partes iguales (bins)
- cada bin tendrá una barra que representa el conteo de ese bin en el eje vertical

## Data proced
En el ejemplo del dataset de canada immigration uaremos los paises como bins y el total como variable contable en eje y

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

```

```python
df_canada['2013'].plot(kind='hist')
plt.title('Histogram of immigration from 195 countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrations')

plt.show()
```

El gráfico anterior tiene el problema de que los ticklabels no están alineados con las barras, para resolver esto definimos los bin_edges y el conteo count

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
```

```python
count, bin_edges = np.histogram(df_canada['2013'])
df_canada['2013'].plot(kind='hist', xticks = bin_edges)
plt.title('Histogram of immigration from 195 countries in 2013')
plt.ylabel('Number of countries')
plt.xlabel('Number of immigrants')

plt.show()
```

