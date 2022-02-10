# Area plots
(Area chart or area graph)
comuntmente usada para representar totales acumulados

## Dataset - Processed
En esta seccion vamos a sacar un dataframe de nuestro tabla de excel para poder ver el total de inmigrantes por pais
y será almacenado en la variable `df_canada`

## Generating Area plots
Para obtener los datos mas significativos ordenaremos a los paises en funcion del numero de inmigrantes total, una vez ordenado de manera descendente podemos ver el top de paises de procedencia del numero de inmigrantes
```python
df_canada.sort_values(['Total'], 
					 ascending = False, 
					 axis = 0, 
					 inplace = True)

```

nota que por la forma (shape) en que fue construido el dataframe, los paises son mostrados en el eje horizontal, para corregir esto se tiene que hacer uso de `Transpose` en el Dataframe para poder ver los paises en el eje vertical

Vamos a generar un dataframe nuevo a partir del que ya teniamos pero ahora solo vamos a incluir los 5 principales paises que nos interesan

```python
years = list(map(str, range(1980, 2014)))

df_canada.sort_values(['Total'], 
					  ascending = False, 
					  axis = 0, 
					  inplace = True)

df_top5 = df_canada.head()
df_top5 = df_top5[years].transpose()
```

## Area plots
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

```python
df_top5.plot(kind='area')

plt.tilte('Immigration trent of top 5 conuntries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()
```
