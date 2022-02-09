# Model evaluation
Model Evaluation nos dice cómo nuestro modelo se forma en el mundo real.
En el módulo anterior, hablamos sobre la evaluación en muestra.
- _La evaluación en muestra_ nos dice qué tan bien nuestro modelo se ajusta a los datos ya dados para entrenarlo.
- _El problema_: No nos da una estimación de qué tan bien puede predecir nuevos datos __el modelo entrenado__ .
- _La solución_: La solución es dividir nuestros datos: 
	- usar los datos de la muestra o los ==datos de entrenamiento== para entrenar el modelo.
	- El resto de los datos llamados ==datos de prueba== se utilizan como datos fuera de muestra. Estos datos luego se utilizan para darnos una idea de cómo se comportaría el modelo en el mundo real.
## Training/Test Sets
Separar los datos en conjuntos __de entrenamiento__ y  __de pruebas__ es una parte importante de la evaluación del modelo.
Utilizamos los datos de prueba para tener una idea de cómo funcionará nuestro modelo en el mundo real.
Cuando dividimos un conjunto de datos, ==generalmente la mayor parte de los datos se usa para entrenamiento y la parte más pequeña se utiliza para las pruebas==.
### Separar el data set:
Por ejemplo, podemos usar el 70% de los datos para el entrenamiento; Luego usamos 30% para las pruebas.
Utilizamos un conjunto de entrenamiento para construir un modelo y descubrir relaciones predictivas.
Luego usamos un conjunto de pruebas para evaluar el rendimiento del modelo.
Cuando hayamos completado la prueba de nuestro modelo, debemos usar todos los datos para entrenarlo.

## Function `train_test_split()`
Una función popular en el paquete de __sci-kit learn__ para dividir conjuntos de datos es la __`train_test_split`__.

```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data,
													y_data, 
													test_size=0.3, 
													random_state=0)
```

Esta función divide aleatoriamente un conjunto de datos en subconjuntos de entrenamiento y prueba.
Como el fragmento de código de ejemplo, este método se importa desde `sklearn.cross validation`.
Los parámetros de entrada ``y_data`` son __la variable objetivo__ (en el ejemplo de evaluación del automóvil,
sería el precio) y ``x_data``, __la lista de variables predictoras__. En este caso, sería todas las otras variables en el conjunto de datos del automóvil que estamos usando para tratar de predecir el _precio_.

![[model_evaluation_0 1.png]]

La salida es una matriz: `x_train` y `y_train`, _los subconjuntos para entrenamiento_; `x_test` y `y_test`, _los subconjuntos para pruebas_. En este caso, el porcentaje `test_size = 0.3` del tamaño de los datos para el conjunto de pruebas. Aquí es del 30%. El estado aleatorio es una semilla aleatoria para una división aleatorea de un conjunto de datos.

## Generalization Performance
El error de generalización es una medida de qué tan bien funcionan nuestros datos al predecir datos que previamente no habian sido vistos.
El error que obtenemos usando nuestros __datos de prueba__ es una aproximación de este error.

### Generalization error
![[model_evaluation_1.png]]
Esta figura muestra la distribución de los __valores reales__ en rojo en comparación con los __valores predichos__ de una regresión lineal en azul.
Vemos que las distribuciones son algo similares.
Si generamos el mismo gráfico usando los __datos de prueba__, vemos que las distribuciones son relativamente diferente.
![[model_evaluation_2.png]]
La diferencia se debe a un __error de generalización__ y representa lo que vemos en mundo real.

## Lots of training data
El uso de una gran cantidad de datos para el entrenamiento nos brinda una media precisa para determinar cómo nuestro modelo
funcionará en el mundo real, pero la precisión del rendimiento será baja.
Aclaremos esto con un ejemplo:
![[model_evaluation_3 1.png]]
El centro de esta diana representa el error de generalización verdadero; digamos que nosotros tomamos una muestra aleatoria de los datos utilizando el 90% de los datos para el entrenamiento y el 10% para las pruebas.
La primera vez que experimentamos obtenemos una buena estimación de los datos de entrenamiento.
Si experimentamos nuevamente, entrenando el modelo con una combinación diferente de muestras, obtendremos tambien un buen resultado, pero los resultados serán diferentes en relación con la primera vez que ejecuta el experimento.
![[lots of training data_1.png]]
Repitiendo el experimento nuevamente con una combinación diferente de entrenamiento y muestras de prueba,
Los resultados son relativamente similares al error de generalización, pero distintos entre sí.
Repitiendo el proceso, obtenemos una buena aproximación de la generalización del error verdadero, pero la precisión es pobre, es decir, todos los resultados son extremadamente diferentes de uno a otro.
![[lots of training data_2.png]]
Si usamos menos puntos de datos para entrenar el modelo y más para probar el modelo, la precisión de el rendimiento de generalización será menor, pero el modelo tendrá buena precisión.

---

La figura de arriba demuestra esto; todas nuestras estimaciones de error están relativamente juntas,
pero están más lejos del verdadero performance de generalización.
Para superar este problema, utilizamos validación cruzada.

## Crossvalidation
Una de las '__métricas de evaluación fuera de muestra__' más comunes es la validación cruzada.
En este método, el conjunto de datos se divide en k grupos iguales; se hace referencia a cada grupo
como un __pliegue__
Por ejemplo 4 pliegues.
![[crossvalidation.png]]
Algunos de los pliegues se pueden usar como un conjunto de entrenamiento, que usamos para entrenar el modelo, y
las partes restantes se usan como un conjunto de prueba, que usamos para probar el modelo.
Por ejemplo, podemos usar tres pliegues para el entrenamiento; luego use un pliegue para probar.
Esto ==se repite hasta que cada partición se use tanto para entrenamiento como para pruebas==.
Al final, usamos los resultados promedio como la estimación del error fuera de la muestra.
La métrica de evaluación depende del modelo.
Por ejemplo, el R cuadrado.

#### Function cross_val_score()
La forma más sencilla de aplicar la validación cruzada es llamar a la función `cross_val_score()`, que realiza múltiples evaluaciones '__fuera de la muestra__'.
Este método se importa del paquete de selección de modelos de sklearn.
Luego usamos la función ``cross_val_score()``. El primer parámetro de entrada es el _tipo de modelo_ que estamos usando para hacer la validación cruzada.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(lr, x_data, y_data, cv=3)
np.mean(scores)
```

En este ejemplo, inicializamos un modelo de regresión lineal u objeto `lr`, que pasamos a la función ``cross_val_score``.
Los otros parámetros son ``x_data``, los datos de la variable de predicción, y ``y_data``, la variable objetivo de los datos.

Podemos gestionar el número de particiones con el parámetro cv.
Aquí, cv = 3, lo que significa que el conjunto de datos se divide en 3 particiones iguales.

La función devuelve una matriz de puntajes, uno para cada partición que se eligió como conjunto de prueba.
Podemos promediar el resultado juntos para estimar R-cuadrado fuera de muestra usando la función ``mean`` en numpy.
Veamos una animación.
Veamos el resultado de la matriz de puntuación en la última diapositiva.
![[cross_val_score1.png]]
Primero, dividimos los datos en tres pliegues. Usamos dos pliegues para el entrenamiento; el restante pliegue para probar.
El modelo producirá una salida.
![[cross_val_score2.png]]
Usaremos la salida para calcular una puntuación. En el caso del R cuadrado, es decir, el coeficiente de determinación, almacenaremos ese valor en una matriz.
Repetiremos el proceso usando dos pliegues para el entrenamiento, y uno para la prueba, guarde el puntaje, luego use una combinación diferente para el entrenamiento y el pliegue restante para las pruebas.
Almacenamos el resultado final.

#### Function cross_val_predict()
La función `cross_val_score()` devuelve un valor de puntuación para indicarnos la validación cruzada resultado.
¿Qué pasa si queremos un poco más de información? ¿Qué pasa si queremos saber la predicción real?
valores proporcionados por nuestro modelo antes de calcular los valores R al cuadrado?
```python
from sklearn.model_selection import cross_val_predict
yhat=cross_val_predict(lr2e, x_data, y_data, cv=3)

```
Para hacer esto, usamos la función `cross_val_predict ()`.
Los parámetros de entrada son exactamente los mismos que la función `cross_val_score()`, pero la salida es una predicción.
Vamos a ilustrar el proceso.
Primero, dividimos los datos en tres pliegues; usamos dos pliegues para entrenar, el pliegue restante para probar.
El modelo producirá una salida y la almacenaremos en una matriz.
Repetiremos el proceso usando dos pliegues para entrenamiento, uno para pruebas.
El modelo produce una salida nuevamente.
Finalmente, usamos los dos últimos pliegues para entrenamiento, luego usamos los datos de prueba.
Este pliegue final de prueba produce una salida.
Estas predicciones se almacenan en una matriz.