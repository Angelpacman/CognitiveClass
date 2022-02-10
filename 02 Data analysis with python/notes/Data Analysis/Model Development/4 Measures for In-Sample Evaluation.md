# Measures for in-Sample Evaluation
Ahora que hemos visto cómo podemos evaluar un modelo mediante la visualización, queremos valuar numéricamente nuestros modelos.
Veamos algunas de las medidas que utilizamos para la evaluación dentro de la muestra.
Estas medidas son una forma de determinar numéricamente qué tan bueno se ajusta el modelo en nuestros datos.
Dos medidas importantes que usamos a menudo para determinar el ajuste de un modelo son: 
- Error cuadrático medio (__MSE__)
- R cuadrado $R^2$ .

## Mean squared error (MSE)
Para medir el #MSE, encontramos la diferencia entre el valor real $y$ y el valor predicho $\hat{y}$ luego elevar al cuadrado el resultado.
![[measures_for_insample_evaluation.png]]
En este caso, el valor real es 150; el valor predicho es 50. Restando estos puntos obtenemos 100.
![[measures_for_insample_evaluations (1).png]]
Luego cuadramos el número.
![[measures_for_insample_evaluations (2).png]]
==Luego tomamos la media o el promedio de todos los errores sumando todos juntos y dividiendo por la cantidad de muestras==.
Para encontrar el MSE en Python, podemos importar el `mean_Squared_error()` de `scikit-learn.metrics`.

La función "`mean_Squared_error()`" obtiene dos entradas: el valor real de la variable objetivo y el valor predicho de la variable objetivo.
```py
from sklearn.metrics import mean_squared_error
mean_squared_error(df['price'], Yhat)
```

## R-squared / $R^2$
==R-cuadrado== también se llama coeficiente de determinación. Es una medida para ==determinar qué tan cerca están los datos de la línea de regresión ajustada==. Entonces, ¿qué tan cerca están nuestros datos reales de nuestro modelo estimado?
Piense en ello como comparar un modelo de regresión con un modelo simple, es decir, la media de los puntos de datos. Si la variable x es un buen predictor, nuestro modelo debería funcionar mucho mejor que con solo la media.

### Coeficiente de determinación R^2 ( $R^2$ )
En este ejemplo, el promedio de los puntos de datos barra 𝑦  es 6.
El coeficiente de determinación o $R^2$ es:
$$
R^2 = \bigl( 1 - \frac{MSE_{ofregressionline} }{MSE_{oftheaverageofthedata}} \bigr)
$$
1 menos la razón del MSE de la regresión lineal dividida por el MSE del promedio de los puntos de datos. En su mayor parte, se necesita
valores entre 0 y 1.
![[measures_for_insample_evaluations (3).png]]
Veamos un caso en el que la línea proporciona un ajuste relativamente bueno.
La línea azul representa la línea de regresión.
Los cuadrados azules representan el MSE de la línea de regresión.
La línea roja representa el valor promedio de los puntos de datos.
Los cuadrados rojos representan el MSE de la línea roja.
Vemos que el área de los cuadrados azules es mucho más pequeña que el área de los cuadrados rojos.
![[measures_for_insample_evaluations (4).png]]
En este caso, debido a que la línea se ajusta bien, el error cuadrático medio es pequeño, por lo tanto el numerador es pequeño.

El error cuadrático medio de la línea es relativamente grande, por lo que el numerador es grande.
Un número pequeño dividido por un número mayor es un número aún menor. 
Llevado a un extremo este valor tiende a cero.
![[measures_for_insample_evaluations (5).png]]
Si conectamos este valor de la diapositiva anterior para $R^2$, obtenemos un valor cercano a uno, esto significa que la línea se ajusta bien a los datos.
![[measures_for_insample_evaluations (6).png]]
Aquí hay un ejemplo de una línea que no se ajusta bien a los datos.
Si solo examinamos el área de los cuadrados rojos en comparación con los cuadrados azules, vemos el área
Es casi idéntico.
La proporción de las áreas es cercana a uno.
En este caso, el $R^2$ está cerca de cero.
Esta línea tiene el mismo rendimiento que usar el promedio de los puntos de datos, por lo tanto, esta línea no funcionó bien.

### R-squared/R^2
```python
X = df[['highway-mpg']]
Y = df[Price]

lm.fit(X,Y)
lm.score(X,Y)
```
output:
`0.496591188`
Encontramos el valor R cuadrado en Python usando el método `score()`, en el objeto regresión lineal.
Del valor que obtenemos de este ejemplo, podemos decir que aproximadamente el __49.695%__ de la la variación del precio se explica por este modelo lineal simple.

==Su valor $R^2$ generalmente está entre 0 y 1, si su $R^2$ es negativo, puede deberse a un sobreajuste== que discutiremos en el próximo módulo.

