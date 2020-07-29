# Análisis de la varianza
En esta sección, estudiaremos el Análisis de #varianza. Supongamos que queremos analizar una variable categórica y ver la correlación entre diferentes categorías.
Por ejemplo, considere el conjunto de datos del automóvil, la pregunta que podemos hacer es, __¿cómo diferentes categorías de la característica__ `make` __(como variable categórica) tiene impacto en__  `price`__?__

![[AVG_price.png]]

El diagrama muestra el precio promedio de diferentes marcas de vehículos.
Para analizar variables categóricas como la variable  `make`, podemos usar un método como el método ANOVA.

ANOVA es una prueba estadística que significa ==Análisis de varianza==.
ANOVA se puede utilizar para encontrar la correlación entre diferentes grupos de una variable categórica.

Según el conjunto de datos del automóvil, podemos usar ANOVA para ver si hay alguna diferencia en la media de `price`s para las diferentes `make` de automóviles como Subaru y Honda.

La prueba ==ANOVA devuelve dos valores: la puntuación de la __prueba F__ y el __valor p.__==

- La prueba F calcula la relación de variación entre la media del grupo sobre la variación dentro de cada uno de los grupos de muestra.
- El valor p muestra si el resultado obtenido es estadísticamente significativo.


Sin profundizar en los detalles, la prueba F calcula la razón de variación entre los promedios de los grupos y la variación dentro de cada una de las medias de las muestras de grupo.

Este diagrama ilustra un caso en el que la puntuación de la prueba F sería pequeña.
Porque, como podemos ver, la variación de los `price`s en cada grupo de datos es mucho mayor que las diferencias entre los valores promedio de cada grupo.

Mirando este diagrama, suponga que el grupo 1 es "Honda" y el grupo 2 es "Subaru"; ambas son las categorías de la feature `make`.
==Como el puntaje F es pequeño, la correlación entre el `price` como la variable objetivo y el agrupamiento son débiles.==

En este segundo diagrama, vemos un caso en el que la puntuación de la prueba F sería grande. La variación entre los promedios de los dos grupos es comparable a las variaciones dentro de los dos grupos.

Suponga que el grupo 1 es "Jaguar" y el grupo 2 es "Honda"; ambos son  categorías de la feature `make`.

Como la ==puntuación F es grande, la correlación es fuerte en este caso.==
Volviendo a nuestro ejemplo, el gráfico de barras muestra el `price` promedio de las diferentes categorías de la feature `make`.

Como podemos ver en el gráfico de barras, esperamos un puntaje F pequeño entre "Hondas" y "Subarus" porque hay una pequeña diferencia entre los `price`s promedio.

Por otro lado, podemos esperar un gran valor F entre Hondas y Jaguars porque las diferencias entre los `price`s es muy significativo.

Sin embargo, de esta tabla no sabemos las variaciones exactas, así que realicemos un ANOVA prueba para ver si nuestra intuición es correcta.

```py
df_anova = df[["make", "price"]]
grouped_anova = df_anova.groupby(['make'])
anova_reults_1 = stats.f_oneway(grouped_anova.get_group('honda')['price'],
								grouped_anova.get_group('subaru')['price'] )
```

- En la primera línea extraemos los datos de `make` y `price`.
- Luego, agruparemos los datos por diferentes marcas.
- La prueba ANOVA se puede realizar en Python usando el método `stats.f_oneway()` como el built-in function del paquete Scipy.

Pasamos los datos de `price`s de los dos grupos de automóviles que queremos comparar y calcula los resultados de ANOVA.

Los resultados confirman lo que adivinamos al principio.
Los `price`s entre Hondas y Subarus no son significativamente diferentes, ya que la puntuación de la prueba F es menor que 1 y el valor p es mayor que 0.05.

Podemos hacer lo mismo para Honda y Jaguar. Los `price`s entre Hondas y Jaguars son significativamente diferentes, ya que el puntaje F es muy grande (F=401) y el valor p es mayor que 0.05.

Con todo, podemos decir que ==existe una fuerte correlación entre una variable categórica y otras variables, si la prueba ANOVA nos da un valor de prueba F grande y un valor p pequeño.==
