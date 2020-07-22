
Una vaz que ya identificamos de que tipo son los abjetos que queremos remplazar (numerico ó categórico) utlizamos el metodo `.replace()` en python usando como argumento los valores que se van a cambiar:

```py
dataframe.replace("valor faltante", "nuevo valor")
```

- Reemplazar faltantes numéricos con el valor promedio de la variable:
```py
mean = df["ventas"].mean()
df["ventas"].replace(np.nan, mean)
```

- Reemplazar faltantes con `NaN`
```py
import pandas as pd
df.replace("?", np.nan, inplace = True)
```
- Contar faltantes por columnas
```py
for column in missing_data.columns.values.tolist():
	print(column)
	print(missing_data["column"].value_counts())
	print(" ")
```