# Model evaluation
Model Evaluation nos dice cómo nuestro modelo se forma en el mundo real.
En el módulo anterior, hablamos sobre la evaluación en muestra.
- La evaluación en muestra nos dice qué tan bien nuestro modelo se ajusta a los datos ya dados para entrenar eso.
- El problema: No nos da una estimación de qué tan bien el modelo capacitado puede predecir nuevos datos.
- La solución: La solución es dividir nuestros datos: 
	- usar los datos de la muestra o los datos de entrenamiento para entrenar el modelo.
	- El resto de los datos llamados datos de prueba se utilizan como datos fuera de muestra. Estos datos luego se utilizan para aproximar cómo se forma el modelo en el mundo real.
## Training/Test Sets
Separar los datos en conjuntos de entrenamiento y pruebas es una parte importante de la evaluación del modelo.
Utilizamos los datos de prueba para tener una idea de cómo funcionará nuestro modelo en el mundo real.
Cuando dividimos un conjunto de datos, generalmente la mayor parte de los datos se usa para entrenamiento y la parte más pequeña se utiliza para las pruebas.
### Separar el data set:
Por ejemplo, podemos usar el 70% de los datos para el entrenamiento; Luego usamos 30% para las pruebas.
Utilizamos un conjunto de entrenamiento para construir un modelo y descubrir relaciones predictivas.
Luego usamos un conjunto de pruebas para evaluar el rendimiento del modelo.
Cuando hayamos completado la prueba de nuestro modelo, debemos usar todos los datos para entrenarlo.

## Function `train_test_split()`
Una función popular en el paquete de aprendizaje sci-kit para dividir conjuntos de datos es la "prueba del tren
"división".
Esta función divide aleatoriamente un conjunto de datos en subconjuntos de entrenamiento y prueba
Desde el fragmento de código de ejemplo, este método se importa desde "sklearn.cross validation".
Los parámetros de entrada y_data son la variable objetivo (en el ejemplo de evaluación del automóvil,
sería el precio) y "x_data", la lista de variables predictoras. En este caso, sería ser todas las otras variables en el conjunto de datos del automóvil que estamos usando para tratar de predecir el precio.

La salida es una matriz: "x_train" y "y_train", los subconjuntos para entrenamiento; "x_test" y "y_test", los subconjuntos para pruebas. En este caso, el porcentaje de "tamaño de prueba" de los datos para el conjunto de pruebas. Aquí es del 30%. El estado aleatorio es una semilla aleatoria para aleatorio
división de conjunto de datos.
## Generalization Performance
El error de generalización es una medida de qué tan bien funcionan nuestros datos al predecir previamente no vistos
datos.
El error que obtenemos usando nuestros datos de prueba es una aproximación de este error.
### Generalization error
Esta figura muestra la distribución de los valores reales en rojo en comparación con los valores predichos valores de una regresión lineal en azul.
Vemos que las distribuciones son algo similares.
Si generamos el mismo gráfico usando los datos de prueba, vemos que las distribuciones son relativamente diferente.
La diferencia se debe a un error de generalización y representa lo que vemos en mundo real.

## Lots of training data
El uso de una gran cantidad de datos para la capacitación nos brinda un medio preciso para determinar cómo nuestro modelo
funcionará en el mundo real, pero la precisión del rendimiento será baja.
Aclaremos esto con un ejemplo.
El centro de esta diana representa el error de generalización verdadero; digamos que nosotros tomamos una muestra aleatoria de los datos utilizando el 90% de los datos para el entrenamiento y el 10% para las pruebas.
La primera vez que experimentamos obtenemos una buena estimación de los datos de entrenamiento.
Si experimentamos nuevamente, entrenando el modelo con una combinación diferente de muestras, obtendremos tambien un buen resultado, pero los resultados serán diferentes en relación con la primera vez que ejecuta el experimento.
Repitiendo el experimento nuevamente con una combinación diferente de entrenamiento y muestras de prueba,
Los resultados son relativamente similares al error de generalización, pero distintos entre sí.
Repitiendo el proceso, obtenemos una buena aproximación de la generalización del error verdadero, pero la precisión es pobre, es decir, todos los resultados son extremadamente diferentes de uno a otro.
Si usamos menos puntos de datos para entrenar el modelo y más para probar el modelo, la precisión de el rendimiento de generalización será menor, pero el modelo tendrá buena precisión.

---

La figura de arriba demuestra esto; todas nuestras estimaciones de error están relativamente juntas,
pero están más lejos del verdadero rendimiento de generalización.
Para superar este problema, utilizamos validación cruzada.

## Crossvalidation
Una de las 'métricas de evaluación fuera de muestra' más comunes es la validación cruzada.
En este método, el conjunto de datos se divide en grupos k-iguales; se hace referencia a cada grupo
como un pliegue
Por ejemplo 4 pliegues.
Algunos de los pliegues se pueden usar como un conjunto de entrenamiento, que usamos para entrenar el modelo, y
las partes restantes se usan como un conjunto de prueba, que usamos para probar el modelo.
Por ejemplo, podemos usar tres pliegues para el entrenamiento; luego use un pliegue para probar.
Esto se repite hasta que cada partición se use tanto para entrenamiento como para pruebas.
Al final, usamos los resultados promedio como la estimación del error fuera de la muestra.
La métrica de evaluación depende del modelo.
Por ejemplo, el R cuadrado.

#### Function cross_val_score()
La forma más sencilla de aplicar la validación cruzada es llamar a la función `cross_val_score()`,
que realiza múltiples evaluaciones 'fuera de la muestra'.
Este método se importa del paquete de selección de modelos de sklearn.
Luego usamos la función cross_val_score(). El primer parámetro de entrada es el tipo de modelo que estamos usando para hacer la validación cruzada.

En este ejemplo, inicializamos un modelo de regresión lineal u objeto lr, que pasamos al
Función cross_val_score.
Los otros parámetros son x_data, los datos de la variable de predicción, y y_data, la variable objetivo de los datos.

Podemos gestionar el número de particiones con el parámetro cv.
Aquí, cv = 3, lo que significa que el conjunto de datos se divide en 3 particiones iguales.
La función devuelve una matriz de puntajes, uno para cada partición que se eligió como conjunto de prueba.
Podemos promediar el resultado juntos para estimar R-cuadrado fuera de muestra usando la función media
en numpy.
Veamos una animación.
Veamos el resultado de la matriz de puntuación en la última diapositiva.
Primero, dividimos los datos en tres pliegues. Usamos dos pliegues para el entrenamiento; el restante
doblar para probar.
El modelo producirá una salida.
Usaremos la salida para calcular una puntuación. En el caso del R cuadrado, es decir, el coeficiente
de determinación
Almacenaremos ese valor en una matriz.
Repetiremos el proceso usando dos pliegues para el entrenamiento, y uno para la prueba,
guarde el puntaje, luego use una combinación diferente para el entrenamiento y el pliegue restante para las pruebas.
Almacenamos el resultado final.

#### Function cross_val_predict()
La función `cross_val_score()` devuelve un valor de puntuación para indicarnos la validación cruzada
resultado.
¿Qué pasa si queremos un poco más de información? ¿Qué pasa si queremos saber la predicción real?
valores proporcionados por nuestro modelo antes de calcular los valores R al cuadrado?
Para hacer esto, usamos la función `cross_val_predict ()`.
Los parámetros de entrada son exactamente los mismos que la función `cross_val_score()`, pero la salida es una predicción.
Vamos a ilustrar el proceso.
Primero, dividimos los datos en tres pliegues; usamos dos pliegues para entrenar, el resto doblar para probar.
El modelo producirá una salida y la almacenaremos en una matriz.
Repetiremos el proceso usando dos pliegues para entrenamiento, uno para pruebas.
El modelo produce una salida nuevamente.
Finalmente, usamos los dos últimos pliegues para entrenamiento, luego usamos los datos de prueba.
Este doblez de prueba final produce una salida.
Estas predicciones se almacenan en una matriz.