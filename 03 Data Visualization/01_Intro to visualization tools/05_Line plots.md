# Line Plots
Este diagrama es un tipo de grafico que muestra informacion de una serie de puntos llamados 'markers' conectados por una linea recta continua que va desde nuestro primer dato hasta el ultimo

## Dataset (recap)
El dataset de canada immigration muestra paises usados como indices y columnas conformados en su mayoria por el año y el numero de immigrants que se registraron en ese año

## Creating Line plots
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

```python
years = list(map(str, range(1980, 2014)))
df_canada.loc['Haiti', years].plot(kind = 'line')
plt.title('Immigration from Haití')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()
```