El objetivo del binning es armar intervalos de  variables numericas para clasificarlas y posteriormente hacer con ello visualización efectiva de los datos

- Agrupar valores en bins (Intervalos)
- Convertir variables numéricas en categóricas
- Agrupar un set de valores numéricas en un set de bins

Una forma rapida de ver una variable en función del conteo de los elementos categóricos que contiene es usar `.hist()` de matplotlib

```py
import matplotlib.pyplot as plt
plt.hist(df["variable"])
```

Para hacerlo desde cero se necesita de `.linspace()`:

```py
#hacer divisiones equidistantes, como necesitamos 3 categorias entonces hacemos 4 diviciones:
bins = np.linspace(min(df['price']), max(df['price']), 4)

#listar los nombres de los grupos:
group_names = ['low', 'medium', 'high']

#armar los bin
df['price_bined'] = pd.cut(	df['price'], 
							bins, 
							labels = group_names, 
							include_lowest = True	)
```
