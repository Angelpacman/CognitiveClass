# Review introduction
Leer un data frame requiere de utilizar la libreria de pandas para ello:
```py
import pandas as pd
```
para abir un csv se usa el metodo de pandas `pd.read_csv()`, por defecto se usa la primera fila del dataset como header, si no queremos tener ningun encabezado usamos la opción: `headers=None`

metodos útiles para la exploracion rapida:

- `df.head()`
- `df.tail()`

Podemos asignar los headers al df con el método `df.columns=headers`, donde headers representa una lista con el nombre de cada columna.

Ejemplo de quitar valores faltantes en una columna con nombre "price" usando en método `.dropna()`:

```py
df.dropna(subset=["price"], axis = 0)
```
---
## Guardar/exportar el dataset:

Se puede sobreescribir el dataframe usado o bien asignarle un nuevo nombre al df con el método `df.to_csv()`

Por defecto este método recibe como argumento el nombre del archvo que se ha de escribir, además de la opción `index = False`

```py
df.to_csv("automobile.csv", index = False)
```

---
## Leer/guardar otros formatos
Data Formate | Read | Save
--------------|-------|------
csv | `pd.read_csv()` | `df.to_csv()`
json | `pd.read_json()` | `df.to_json()`
excel | `pd.read_excel()` | `df.to_excel()`
hdf | `pd.read_hdf()` | `df.to_hdf()`
sql | `pd.read_sql()` | `df.to_sql()`

---
## Descripción de los datos
- `df.dtypes`: Describe los tipos de objetos en el df.
- `df.info` and `df.info()`: ambos métodos dan un conteo de los elementos en las columnas asi como señalar su tipo de objeto.
- `df.describe`: Hace un resumen estadistico de todas las columnas ([[Feature]]) en el dataframe excluyendo por defecto los valores faltantes ^[Tambien conocidos como "missing values", estos valores faltantes suelen pasarse a formato de pandas como NaN (Not a Number) con la funcion `np.nan()` ], si se queren considerar todos los datos se agrega el argumento `include = "all"` aunque esto resulta que las operaciones matempaticas que tengan que ver con un `NaN` resultan en `NaN`.

La desccripción de solo algunas columnas se puede hacer seleccionando el label del df y aplicando al final el método `.describe()`, ejemplo:
```py
df[["columna 1", "columna 3"]].describe()
```

