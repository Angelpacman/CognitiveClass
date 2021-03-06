# Estadística descriptiva
Cuando comience a analizar datos, es importante explorar primero sus datos antes de gastar tiempo construyendo modelos complicados. Una manera fácil de hacerlo es calcular algunos estadísticas descriptivas para sus datos.

El análisis estadístico descriptivo ayuda a describir las características básicas de un conjunto de datos y obtiene un breve resumen sobre la muestra y las medidas
de los datos.

Vamos a mostrarte un par de útiles diferentes métodos. Una forma en que podemos hacer esto es mediante el uso de la función `.describe()` en **pandas**.

Usando la función describe y aplicándola en su marco de datos (data frame), la función `.describe()` calcula automáticamente estadísticas básicas para todas las variables numéricas. Muestra la media, el número total de datos, puntos, la desviación estándar, los cuartiles y los valores extremos.

Cualquier valor de NaN se omite automáticamente en estas estadísticas. Esta función te dará una idea más clara de la distribución de tus diferentes variables.

## Conteo de categorías

También podrías tener variables categóricas en tu conjunto de datos. Estas son variables que se pueden dividir en diferentes categorías o grupos y tienen valores discretos. Por ejemplo, en nuestro conjunto de datos tenemos la `unidad sistema` como una __variable categórica__, que consta de las categorías: _tracción delantera, rueda trasera, unidad y tracción en las cuatro ruedas_.

Una forma de resumir lo categórico los datos son mediante el uso de la función `.value_counts()`. Podemos cambiar el nombre de la columna para hacer
Es más fácil de leer:

```py
#hacer un conteo de las variables y pasarlas a una tabla
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()

#renombrar la columna y el index
drive_wheels_counts.rename(	columns={'drive-wheels':'value_counts'},
							inplace=True )
drive_wheels_counts.index.name = 'drive-wheels'
```

-|value_counts
-----|-----
drive-wheels | -
fwd | 118
rwd | 75
4wd | 8

Vemos que tenemos 118 autos en el __fwd__ (frente categoría de tracción en las ruedas), 75 autos en la categoría __rwd__ (tracción en las ruedas traseras) y 8 autos en la categoría __4wd__ (tracción a las cuatro ruedas).

## Boxplot

Los diagramas de caja son una excelente manera de visualizar numéricos datos, ya que puede visualizar las diversas distribuciones de los datos.

Las características principales que muestra el diagrama de caja son la #mediana de los datos, que representa dónde está el punto medio de datos. El cuartil superior muestra dónde está el percentil 75 es decir, el cuartil inferior muestra dónde está el percentil 25. Los datos entre el Superior y el cuartil inferior representa el __rango intercuartil__.

A continuación, tienes los extremos inferior y superior. Estos se calculan como 1.5 veces el rango intercuartil por encima del percentil 75, y como 1,5 veces el IQR por debajo del percentil 25.

Finalmente, los gráficos de caja también muestran valores atípicos como puntos individuales que ocurren fuera de la parte superior y extremos inferiores. Con las gráficas de caja, puede detectar fácilmente valores atípicos y también ver la distribución y el sesgo de los datos.

Los diagramas de caja facilitan la comparación entre grupos. En este ejemplo, usando Boxplot podemos ver la distribución de diferentes categorías de la característica de `drive-wheels` sobre la característica `price`.
```py
sns.boxplot(x = "drive-wheels", y = "price", data=df)
```

Podemos ver que la distribución del `price` entre el rwd (tracción trasera) y las otras categorías son distintas, pero el `price` para fwd (tracción delantera) y 4wd (tracción a las cuatro ruedas) son casi indistinguibles.

## Scatterplot

Muchas veces tendemos a ver variables continuas en nuestros datos. Estos puntos de datos son números contenidos en algún rango. Por ejemplo, en nuestro conjunto de datos, `price` y `engine-size` son variables continuas. ¿Qué pasa si queremos entender la relación entre `engine-size` y `price`? ¿Podría el `engine-size` predecir el `price` de un auto?

Una buena forma de visualizar esto es usar un gráfico de dispersión. Cada observación en un diagrama de dispersión está representada como un punto. Este gráfico muestra la relación entre dos variables:

- La ==variable predictora==: es la variable que está utilizando para predecir un resultado. En este caso, nuestra variable predictora es el `engine-size`.

- La ==variable objetivo==: es la variable que está intentando predecir. En este caso, nuestra variable objetivo es `price`, ya que este sería el resultado.

En un diagrama de dispersión, generalmente establecemos la variable predictiva en el eje x o el eje horizontal y establecemos la variable objetivo en el eje y o eje vertical.

En este caso, trazaremos el `engine-size` en el __eje x__ y el `price` en el __eje y__.

Estamos usando la función "dispersión" de Matplotlib `plt.scatter()` aquí, tomando en x y una variable y algo a tener en cuenta es que siempre es importante etiquetar los ejes y escribir un diagrama general título, para que sepa lo que está mirando.
![[scatter-Enginesize-price.png]]

Ahora, ¿cómo se relaciona la variable `engine-size` con el `price`? Desde el diagrama de dispersión vemos que a medida que aumenta el `engine-size`, el `price` del automóvil también aumenta.

Esto nos está dando una indicación inicial de que existe una relación lineal positiva entre estas dos variables.

---
Ahora que hemos obtenido un panorama general de nustros datos con la estadistica descriptiva, toca tratar los datos con [[2 GroupBy| Agrupaciones por columnas]]
