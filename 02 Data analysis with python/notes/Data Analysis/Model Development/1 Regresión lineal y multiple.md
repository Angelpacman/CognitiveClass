## Regresión lineal y regresión lineal multiple
- La regresión lineal se referirá a una variable independiente para hacer una predicción.
- La regresión lineal múltiple se referirá a múltiples variables independientes para hacer una predicción.

La regresión lineal simple (o SLR) es: Un método para ayudarnos a comprender la relación entre dos variables: la ==variable predictora==(independiente) $x$, y la ==variable objetivo== (dependiente) $y$.

Nos gustaría llegar a una relación lineal entre las variables que se muestran aquí:

$y = b_{0} + b_{1} * x$
- El parámetro $b_{0}$ es la intersección
- El parámetro $b_{1}$ es la pendiente. 

Cuando ajustamos o entrenamos el modelo, llegaremos arriba con estos parámetros. Este paso requiere muchas matemáticas, por lo que no nos centraremos en esto parte. Aclaremos el paso de predicción. 
Es difícil calcular cuánto cuesta un automóvil, pero las millas de autopista por galón se encuentran en el manual del propietario. Si asumimos, hay un relación lineal entre estas variables, podemos usar esta relación para formular un modelo para determinar el precio del automóvil. Si las millas de autopista por galón son 20, nosotros podemos ingresar su valor en el modelo para obtener una predicción de $22,003.

$y = 38423 - 821x$
$y = 38423 - 821(20)$
$y = 22003$

### Fit (Ajuste)
Para determinar la línea, tomamos puntos de datos de nuestro conjunto de datos marcados en rojo aquí.
Luego usamos estos puntos de entrenamiento para ajuetar nuestro modelo; ==los resultados de los puntos de entrenamiento son los parámetros( $b_{0}$ y $b_{1}$ )==. Generalmente almacenamos los puntos de datos en dos dataframe o matrices numpy(_arrays_). 

El valor que nos gustaría predecir se llama el _objetivo_, mismo que almacenamos en la matriz $Y$, almacenamos la _variable dependiente_ en el dataframe o matriz $X$. Cada muestra corresponde a una fila diferente en cada dataframe o matriz. 

En muchos casos, muchos factores influyen en cómo mucha gente paga por un automóvil, por ejemplo, la marca o la antigüedad del automóvil. En este modelo, esta incertidumbre se tiene en cuenta suponiendo que se agrega un pequeño valor aleatorio al punto
en la línea; Esto se llama ruido. 

La figura de la izquierda muestra la distribución del ruido, El eje vertical muestra el valor agregado y el eje horizontal ilustra la probabilidad de que se agregue el valor. Por lo general, se agrega un pequeño valor positivo, o un pequeño valor negativo. A veces se agregan valores grandes, pero en su mayor parte, los valores agregados son cercanos a cero. 

Podemos resumir el proceso así:
- Tenemos un conjunto de puntos de entrenamiento 
- Usamos estos puntos de entrenamiento para encajar o entrenar el modelo y obtener parámetros: luego usamos estos parámetros en el modelo
- Ahora tenemos un modelo; usamos el sombrero en la $y$ para denotar que el modelo es una estimación:
	$\hat{y} = b_{0} + b_{1} * x$
- Podemos usar este modelo para predecir valores que no hemos visto.

Por ejemplo, no tenemos un automóvil con 20 millas de autopista por galón, podemos usar nuestro modelo para hacer una predicción para el precio de este automóvil. Pero no olvide que nuestro modelo no siempre es correcto.

Podemos ver esto comparando el valor predicho con el valor real.
Tenemos una muestra de 10 millas de autopista por galón, pero el valor predicho no coincide con el valor real. Si la suposición lineal es correcta, este error se debe al ruido pero puede haber otras razones.

1. Para ajustar el modelo en Python, primero importamos el modelo lineal de scikit-learn; 
```py
from sklearn.linear_model import LinearRegression
```
2. Luego crear un objeto de regresión lineal usando el constructor. 
```py
lm = LinearRegression()
```

3. Definimos la variable predictiva y la variable objetivo.
```py
X = df[['highway-mpg']]
Y = df['price']
```
4. Luego use el método fit para ajustar el modelo y encontrar los parámetros $b_{0}$ y $b_{1}$. La entrada son las características y los objetivos.
```py
lm.fit(X,Y)
```
5. Podemos obtener una predicción usando el método predic.
```py
Yhat = lm.predict(X)
```
La salida es una matriz, la matriz tiene el mismo número de muestras que la entrada X.
Yhat | X
-----|----
2 	| 5
... | ...
3 | 4

==La intersección $b_0$ es un atributo del objeto lm== `lm.intercept_`
==La pendiente $b_1$ también es un atributo del objeto lm== `lm.coef_`

La relación entre `price` y `highway-mpg` viene dada por esta ecuación en negrita: 
$Precio = 38,423.31 - 821.73 * mpg_{highway}$ como la ecuación que discutimos antes.

### Regresión lineal multiple
La regresión lineal múltiple se utiliza para explicar la relación entre
- Una variable objetivo (Y) continua, y 
- Dos o más variables predictoras (X).

Si tenemos por ejemplo 4 variables predictoras, 
$\hat{y} = b_0+b_1*x_1+b_2*x_2+b_3*x_3+b_4*x_4$

entonces:
- $b_0$: intercepción (X = 0) 
- $b_1$: el coeficiente o parámetro de 𝑋1:
- $b_2$: el coeficiente del parámetro 𝑋2: y así sucesivamente

Si solo hay dos variables, podemos visualizar los valores. Considere la siguiente función.
$\hat{y} = 1 + 2*x_1 + 3*x_2$

Las variables 𝑋1 y 𝑋2 se pueden visualizar en un plano 2D; hagamos un ejemplo. 
La tabla contiene diferentes valores de variables predictoras 𝑋1 y 𝑋2. La posición de cada punto se coloca en el plano 2D, color codificado en consecuencia. Cada valor de las variables predictoras 𝑋1 y 𝑋2 se asignará a un nuevo valor 𝑌 ($\hat{y}$ predecida)

Se asignarán los nuevos valores de 𝑌 ($\hat{y}$ predecida) en la dirección vertical, con altura proporcional al valor que toma.

Podemos ajustar la regresión lineal múltiple de la siguiente manera:
- Podemos extraer las 4 variables predictoras y almacenarlas en la variable Z.
```py
Z = df[['horesepower', 'crumb-weight', 'engine-size', 'highwat-mpg']]
```
- Luego entrenar el modelo como antes de usar el método de entrenamiento, con las características o variables dependientes
```py
lm.fit(Z, df['price'])
```
y los objetivos: (dos puntos)
- También podemos obtener una predicción usando el método de predicción. 
```py
Yhat = lm.predict(X)
```
En este caso, la entrada es una matriz o marco de datos con 4 columnas, 
El número de filas corresponde al número de muestras.
$x_1$ | $x_2$ | $x_3$ | $x_4$
----|----|-----------|----
3 | 5 |-4| 3
...|...|...|...
2|4 |2|-4

La salida es una matriz con el mismo número de elementos que el número de muestras.
|Yhat|
|----|
|2|
|...|
|3|

1. La intersección es un atributo del objeto `lm.intercept_`. Y los coeficientes también son atributos `lm.coef_`.
1. Es útil visualizar la ecuación, reemplazando los nombres de las variables dependientes con nombres reales.
Esto es idéntico al formulario que discutimos anteriormente.
