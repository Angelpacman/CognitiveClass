Luego de que nos aseguramos de tratar a los datos faltantes, hay que verificar su tipo de dato y corregirlo de ser necesario: 

- `.dtype()` y `.dtypes`: Examinan el tipo de dato
- `.astype()`: Cambia el tipo de dato usando como argumento un tipo diferente ( `float`, `int`, `datetime`, etc )
- `.info()`: Proporciona informacion sobre todo el dataframe, conteo de variables, faltantes y tipo de objeto.

---
### Estandarización de los datos
La estandarizacion es el proceso de transformar datos en formato común y consistente, por ejemplo:

Trabajar con 1 sólo nombre para referirnos a una variable

Raw Data | Estandarizados
----------|-----------------
Ny | New york
N.Y | New york
NEW York | New york
NY. | New york

De ser necesario cambiar unidades al S.I. asi como el nombre de la variable en el df:
```py
df ["highway-L/100km"] = 235/df["highway-mpg"]
df.rename(columns = {'highway-mpg':'highway-L/100km'}, inplace = True)
```