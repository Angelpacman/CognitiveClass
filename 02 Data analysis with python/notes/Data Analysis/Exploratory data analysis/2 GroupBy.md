# Agrupación por caracteristicas
En esta sección cubriremos los conceptos básicos de la agrupación y cómo esto puede ayudar a transformar nuestro conjunto de datos.

Suponga que quiere saber: ¿Existe alguna relación entre los diferentes tipos de **sistema de accionamiento**? (adelante, atrás y tracción a las cuatro ruedas) y el `price` de los vehículos?

Si es así, ¿qué tipo de "sistema de conducción" agrega más valor a un vehículo?
Sería bueno si pudiéramos agrupar todos los datos por los diferentes tipos de `drive-wheels`, y compare los resultados de estas diferentes `drive-wheels` entre sí.

En pandas esto se puede hacer usando el grupo por método **GroupBy**.
- El grupo por característica se utiliza en variables categóricas
- Agrupa los datos en subconjuntos según a las diferentes categorías de esa variable.
- Puede agrupar por una sola variable o puede agrupar por múltiples variables pasando múltiples nombres de variables.

Como ejemplo, digamos que estamos interesados en encontrar el `price` promedio de vehículos y observe cómo difieren las variables entre los diferentes tipos de `body-style` y `drive-wheels`

Para hacer esto, primero seleccionamos las tres columnas de datos que nos interesan, lo que se haceen la primera línea de código.
```py
df_gptest = df[['drive-wheels','body-style','price']]
```
Luego agrupamos los datos reducidos de acuerdo con `drive-wheels` y `body-style` en la segunda línea.
```py
grouped_test1 = df_gptest.groupby([	'drive-wheels',
									'body-style'],
									as_index=False).mean()
```


Como estamos interesados en saber cómo difiere el `price` promedio en todos los ámbitos, puede tomar la media de cada grupo y agregar este bit al final de la línea 2.

```py
grouped_test1
```

output:

 -| drive-wheels |	body-style | price
 --|--------------|-------------|---
0 |	4wd |	hatchback |	7603.000000
1 |	4wd |	sedan 	|12647.333333
2| 	4wd |	wagon 	|9095.750000
3 |	fwd | convertible 	|11595.000000
4 |	fwd |	hardtop 	|8249.000000
5 |	fwd |	hatchback 	|8396.387755
6 |	fwd |	sedan 	|9811.800000
7 |	fwd |	wagon 	|9997.333333
8 |	rwd |	convertible 	|23949.600000
9 |	rwd |	hardtop 	|24202.714286
10| rwd |	hatchback |	14337.777778
11 |	rwd | sedan 	|21711.833333
12 |	rwd | wagon	|16994.222222

Los datos ahora se agrupan en subcategorías y solo es mostrado el `price` promedio de cada subcategoría.

Podemos ver que, de acuerdo con nuestros datos, los convertibles de tracción trasera y la tracción trasera los hardtops tienen el valor más alto, mientras que los hatchbacks con tracción en las cuatro ruedas tienen el valor más bajo.

Una tabla de este formulario no es la más fácil de leer y tampoco es muy fácil de visualizar.

## Pivot

Para que sea más fácil de entender, podemos transformar esta tabla en una tabla dinámica mediante el uso del método tabla dinámica `.pivot()`.

En la tabla anterior, las `drive-wheels` y el `body-style` se enumeraron en columnas. Una tabla dinámica tiene una variable mostrada a lo largo de las columnas y la otra variable mostrada a lo largo de las filas.

```py
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
```
  | |`price`|`price` |`price` |`price`  |`price`
---|---|---|---|---|---
`body-style` |convertible |hardtop |hatchback |sedan |wagon
`drive-wheels`| | | | |
4wd 	|NaN| 	NaN| 	7603.000000| 	12647.333333 |	9095.750000
fwd 	|11595.0| 	8249.000000| 	8396.387755 |	9811.800000 |	9997.333333
rwd 	|23949.6| 	24202.714286| 	14337.777778 |	21711.833333 |16994.222222

Solo con una línea de código y usando el método de `.pivot()` de pandas, podemos pivotar la variable  `'body-style'` para que se muestre a lo largo de las columnas y las " `drive-wheels` " se mostrará a lo largo de las filas.

Los datos de `price`s ahora se convierten en una cuadrícula rectangular, que es más fácil de visualizar. Esto es similar a lo que generalmente se hace en las hojas de cálculo de Excel.

## Heat map

Otra forma de representar la tabla dinámica es usar un diagrama de mapa de calor ==Heat map==. El mapa de calor toma una cuadrícula de datos rectangular y asigna una intensidad de color basada en el valor de datos en los puntos de la cuadrícula.

Es una excelente manera de trazar la **variable objetivo** sobre múltiples variables y, a través de esto, obtener pistas visuales de la relación entre estas variables y el objetivo.
##### Example
En este ejemplo, utilizamos el método pcolor de `pyplot` para trazar un mapa de calor y convertir el tabla dinámica anterior en una forma gráfica.

==Especificamos el esquema de color rojo-azul==(aunque se puede usar color 'jet')
```py
#figura
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
```
![[heatmap.png]]
En la gráfica de salida, cada tipo de `body-style` está numerado a lo largo del **eje x** y cada tipo de `drive-wheels` está numerado a lo largo del **eje y**.

Los `price`'s promedio se trazan con diferentes colores en función de sus valores, de acuerdo con la barra de colores. Vemos que la sección superior del mapa de calor parece tener `price`'s más altos que la parte inferior sección.

El mapa de calor traza la variable objetivo (`price`) proporcional al color con respecto a las variables '`drive-wheels`' y '`body-style`' en los ejes vertical y horizontal, respectivamente. Esto nos permite visualizar cómo se relaciona el `price` con '`drive-wheels`' y '`body-style`'.

Las etiquetas predeterminadas no nos transmiten información útil. Cambiemos eso:
```py
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1] #levels no es necesario si no son datos de una tabla pivotada, es decir el "label" esta bien definido
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()
```

![[heatmap labeled.png]]

---
Ahora que tenemos un panorama de los datos a partir de un par de variables predictoras y una variable objetivo toca tratar los datos con el [[3 ANOVA|Análisis de la varianza]]