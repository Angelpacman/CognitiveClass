En esta sección, estudiaremos el Análisis de varianza. Supongamos que queremos analizar una variable categórica y ver la correlación entre diferentes categorías.
Por ejemplo, considere el conjunto de datos del automóvil, la pregunta que podemos hacer es, __¿cómo diferentes categorías de la característica `make` (como variable categórica) tiene impacto en  `price`?__

El diagrama muestra el precio promedio de diferentes marcas de vehículos.
Vemos una tendencia de aumento de los `price`s a medida que avanzamos a lo largo del gráfico. Pero, ¿qué categoría en la función de creación tiene más y cuál tiene el menor impacto en la predicción del  `price` del automóvil?
Para analizar variables categóricas como el "`make`" variable, podemos usar un método como como el método ANOVA.

ANOVA es una prueba estadística que significa =="Análisis de varianza"==.
ANOVA se puede utilizar para encontrar la correlación entre diferentes grupos de una variable categórica.

Según el conjunto de datos del automóvil, podemos usar ANOVA para ver si hay alguna diferencia en la media `price` para las diferentes marcas de automóviles como Subaru y Honda.

La prueba ANOVA devuelve dos valores: la puntuación de la prueba F y el valor p.
La prueba F calcula la relación de variación entre la media del grupo sobre la variación dentro de cada uno de los grupos de muestra.

El valor p muestra si el resultado obtenido es estadísticamente significativo.
Sin profundizar en los detalles, la prueba F calcula la relación de variación entre
grupo significa sobre la variación dentro de cada una de las medias del grupo muestra.

Este diagrama ilustra un caso en el que la puntuación de la prueba F sería pequeña.
Porque, como podemos ver, la variación de los `price`s en cada grupo de datos es mucho mayor que las diferencias entre los valores promedio de cada grupo.

Mirando este diagrama, suponga que el grupo 1 es "Honda" y el grupo 2 es "Subaru"; ambas son las categorías de funciones de creación.
Como el puntaje F es pequeño, la correlación entre el `price` como la variable objetivo y el Las agrupaciones son débiles.

En este segundo diagrama, vemos un caso en el que la puntuación de la prueba F sería grande. La variación entre los promedios de los dos grupos es comparable a las variaciones dentro de los dos grupos.

Suponga que el grupo 1 es "Jaguar" y el grupo 2 es "Honda"; ambos son la función `make` categorías.

Como la puntuación F es grande, la correlación es fuerte en este caso.
Volviendo a nuestro ejemplo, el gráfico de barras muestra el `price` promedio de las diferentes categorías de la función de hacer.

Como podemos ver en el gráfico de barras, esperamos un pequeño puntaje F entre "Hondas" y "Subarus" porque hay una pequeña diferencia entre los `price`s promedio.

Por otro lado, podemos esperar un gran valor F entre Hondas y Jaguars porque las diferencias entre los `price`s es muy significativo.

Sin embargo, de esta tabla no sabemos las variaciones exactas, así que realicemos un ANOVA prueba para ver si nuestra intuición es correcta.

En la primera línea extraemos los datos de marca y `price`.
Luego, agruparemos los datos por diferentes marcas.
La prueba ANOVA se puede realizar en Python usando el método f_oneway como el incorporado función del paquete Scipy.

Pasamos los datos de `price`s de los dos grupos de automóviles que queremos comparar y calcula
Los resultados de ANOVA.
Los resultados confirman lo que adivinamos al principio.
Los `price`s entre Hondas y Subarus no son significativamente diferentes, ya que la prueba F
la puntuación es menor que 1 y el valor p es mayor que 0.05.
Podemos hacer lo mismo para Honda y Jaguar.
Los `price`s entre Hondas y Jaguars son significativamente diferentes, ya que el puntaje F
es muy grande (F u003d 401) y el valor p es mayor que 0.05.
Con todo, podemos decir que existe una fuerte correlación entre una variable categórica
y otras variables, si la prueba ANOVA nos da un valor de prueba F grande y un valor p pequeño.
