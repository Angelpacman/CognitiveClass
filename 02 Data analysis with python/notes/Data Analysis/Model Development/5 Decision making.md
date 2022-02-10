# Prediction and decision making
En esta sección, nuestro tema final será sobre predicción y toma de decisiones: ¿cómo podemos determinar si nuestro modelo es correcto?
Lo primero que debe hacer es asegurarse de que los resultados de su modelo tengan sentido.
Siempre debe usar la visualización, las medidas numéricas para la evaluación y la comparación entre diferentes modelos.
## Do the predicted values make sense?
Veamos un ejemplo de predicción; si recuerdas, entrenamos el modelo usando el método de ajuste `fit`.
```py
im.fit(df['highway-mpg'], df['prices'])
```
Ahora queremos saber cuál sería el precio de un automóvil que tiene un `highway-mpg` de _30_. Al conectar este valor al método `predict()`, nos da un precio resultante de _3,771.30_.
```py
lm.predict(30)
```
Esto parece tener sentido, por ejemplo, el valor no es negativo, extremadamente alto o extremadamente bajo.
Podemos observar los coeficientes examinando el atributo `coef_`.
Si recuerdas la expresión para el modelo lineal simple que predice el precio de `highway-mpg`
$$
Price = 38423.31 - 821.73 * highway_{mpg}
$$

Este valor corresponde al múltiplo de la característica `highway-mpg`.
Como tal, un aumento de una unidad en mpg en carretera, el valor del automóvil disminuye aproximadamente 821 dólares; Este valor también parece razonable. 
A veces su modelo producirá valores que no tienen sentido, por ejemplo, si trazamos En el modelo para mpg en carretera, en los rangos de 0 a 100, obtenemos valores negativos para precio.
Esto podría deberse a que los valores en ese rango no son realistas, el supuesto lineal es incorrecto, o no tenemos datos para automóviles en ese rango.
En este caso, es poco probable que un automóvil tenga un millaje de combustible en ese rango, por lo que nuestro modelo Parece valido.

Para generar una secuencia de valores en un rango específico, importe numpy, luego use la función `array` de numpy para generar la secuencia.
```py
import numpy as np
new_input = np.arange(1,101,1).reshape(-1,1)
```
La secuencia comienza en uno y se incrementa en uno hasta llegar a 100.
El primer parámetro es el punto de partida de la secuencia.
El segundo parámetro es el punto final más uno de la secuencia.
El parámetro final es el tamaño del paso entre los elementos de la secuencia, en este caso, es uno, entonces incrementamos la secuencia paso a paso, de 1 a 2, y así sucesivamente.
Podemos usar la salida para predecir nuevos valores; la salida es una matriz de numpy.
Muchos de los valores son negativos.

### Visualization
Usar un gráfico de regresión para visualizar sus datos es el primer método que debe probar.
Consulte los laboratorios para ver ejemplos de cómo trazar una regresión polinómica.
Para este ejemplo, el efecto de la variable independiente es evidente en este caso.
La tendencia de los datos disminuye a medida que aumenta la variable dependiente.
El gráfico también muestra un comportamiento no lineal.
Examen de la trama residual Vemos en este caso que los residuos tienen una curvatura sugiriendo un comportamiento no lineal.
Un diagrama de distribución es un buen método para la regresión lineal múltiple.
Por ejemplo: vemos los valores pronosticados para los precios en
el rango de 30000 a 50,000 son inexactos Esto sugiere que un modelo no lineal puede ser más adecuado o necesitamos más datos en este rango.

## Numerical measures for evaluation
El error cuadrático medio es quizás la medida numérica más intuitiva para determinar si un modelo es bueno o no; veamos cómo impactan diferentes medidas de error cuadrático medio el modelo.

La figura muestra un ejemplo de un error cuadrático medio de 3.495.
Este ejemplo tiene un error cuadrático medio de 3,652.
La trama final tiene un error cuadrado medio de 12870.
A medida que aumenta el error cuadrado, los objetivos se alejan de los puntos predichos.
Como discutimos, R ^ 2 (R-cuadrado) es otro método popular para evaluar su modelo.
En esta gráfica, vemos los puntos objetivo en rojo y la línea pronosticada en azul, un R ^ 2 de 0.9986; El modelo parece ser un buen ajuste.
Este modelo tiene un R ^ 2 de 0.9226; Todavía hay una fuerte relación lineal.
Un R ^ 2 de 0806 los datos son mucho más desordenados pero la relación lineal es evidente.
Un R ^ 2 de 0.61 la función lineal es más difícil de ver, pero, en una inspección más cercana, vemos que los datos están aumentando con la variable independiente.
Un valor aceptable para R ^ 2 depende del campo que esté estudiando.
Algunos autores sugieren que un valor debe ser igual o mayor que 0.10.

## Comparando MLR y SLR

¿Un MSE más bajo siempre implica un mejor ajuste?
No necesariamente.
==MSE para un modelo MLR será más pequeño que el MSE para un modelo SLR==, ya que los errores de los datos disminuirá cuando se incluyan más variables en el modelo.
La regresión polinómica también tendrá un MSE más pequeño que la regresión regular.
Una relación inversa similar es válida para R ^ 2.
En la siguiente sección veremos mejores formas de evaluar el modelo.