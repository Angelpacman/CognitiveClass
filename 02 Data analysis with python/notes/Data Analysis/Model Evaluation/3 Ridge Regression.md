# Ridge Regression
En esta seccion, analizaremos la regresión de crestas. La regresión de la cresta evita un ajuste excesivo ( #Sobreajuste ).
Nos centraremos en la regresión polinomial para la visualización, pero el sobreajuste también es un gran problema cuando tiene múltiples variables o características independientes.
Considere el siguiente polinomio de cuarto orden en naranja. 
$$y = 1 + 2x -3x^2 -4x^3 +4x^4$$
![[ridge_regression (1).png]]
Los puntos azules se generan a partir de
esta función. Podemos usar un polinomio de décimo orden para ajustar los datos. 
![[ridge_regression (2).png]]
La función estimada en el azul hace un buen trabajo al aproximarse a la función verdadera.
![[ridge_regression (3).png]]
En muchos casos, los datos reales tienen valores atípicos. Por ejemplo, este punto que se muestra aquí no aparece que proceda de la función en naranja. 
![[ridge_regression (4).png]]
Si usamos una función polinomial de décimo orden para ajustar los datos, la función estimada en azul es incorrecta y no es una buena estimación de la función actual en naranja.
![[ridge_regression (5).png]]
Si examinamos la expresión de la función estimada, vemos el polinomio estimado los coeficientes tienen una magnitud muy grande. 
![[ridge_regression (6).png]]
Esto es especialmente evidente para los orden polinomios. La regresión de crestas controla la magnitud de estos coeficientes polinomiales introduciendo el parámetro alpha #ParameterAlpha.
Alpha es un parámetro que seleccionamos antes de ajustar o entrenar el modelo. Cada fila en la siguiente tabla representa un valor creciente de alfa.
![[ridge_regression (7).png]]
Veamos cómo los diferentes valores de alfa cambian el modelo.
![[ridge_regression (8).png]]
Esta tabla representa los coeficientes polinomiales para diferentes valores de alfa. Las columnas corresponden a los diferentes coeficientes polinomiales y las filas corresponden a los diferentes valores de alfa. A medida que aumenta alfa, los parámetros se vuelven más pequeños. 
![[ridge_regression (9).png]]
Esto es más evidente para características polinomiales de orden superior, pero alfa debe seleccionarse con cuidado. Si alfa es demasiado grande, los coeficientes se acercarán a cero y no se ajustarán a los datos.
![[ridge_regression (10).png]]
Si alfa es cero, el ajuste excesivo es evidente. 
![[ridge_regression (11).png]]
Para alfa igual a 0,001, el sobreajuste comienza a disminuir. 
![[ridge_regression (12).png]]
Para alfa igual a 0.01, la función estimada rastrea la función real. 
![[ridge_regression (13) 1.png]]
Cuando alfa es igual a 1, vemos los primeros signos de debajo del ajuste. La función estimada no tiene suficiente flexibilidad.
![[ridge_regression (14).png]]
En alfa igual a 10, vemos un ajuste insuficiente extremo; ni siquiera rastrea los dos puntos.
##### Code Ridge Regression
Para seleccionar alfa usamos validación cruzada.
```py
from sklearn.linear_model import Ridge
RidgeModel = Ridge(alpha = 0.1)
RidgeModel.fit(X,y)
Yhat = RidgeModel.predict(X)
```
Para realizar una predicción mediante la regresión de crestas, importe crestas de modelos lineales sklearn. Crear un objeto Ridge usando el constructor. El parámetro alfa es uno de los argumentos de el constructor. Entrenamos el modelo usando el método de ajuste. Para hacer una predicción, usamos
el método de predicción.
![[ridge_regression (15).png]]
Para determinar el __parámetro alfa__, usamos algunos datos para el entrenamiento. Usamos un segundo conjunto llamado __datos de validación__; esto es similar a los datos de prueba, pero se usa para seleccionar parámetros como alfa. Comenzamos con un pequeño valor de alfa, entrenamos el modelo, hacemos una predicción utilizando los datos de validación, luego calcule R cuadrado y almacene los valores. Repetir el valor de un valor mayor de alfa. Entrenamos el modelo nuevamente, hacemos una predicción usando los datos de validación, luego calcule R cuadrado y almacene los valores de R cuadrado.
Repetimos el proceso para un valor alfa diferente, entrenamos el modelo y hacemos una predicción.
Seleccionamos el valor de alfa que maximiza la R al cuadrado. Tenga en cuenta que ==podemos utilizar otras métricas para seleccionar el valor de alfa== como el error cuadrático medio.
El problema del sobreajuste es aún peor si tenemos muchas funciones. La siguiente trama muestra los diferentes valores de R al cuadrado en el acceso vertical. 
![[ridge_regression (16).png]]
El eje horizontal representa diferentes valores para alfa.
Usamos varias características de nuestro conjunto de datos de autos usados y una función polinomial de segundo orden.
Los datos de entrenamiento están en rojo y los datos de validación están en azul. 
![[ridge_regression (17).png]]
Vemos como el valor de alfa aumenta, el valor de R al cuadrado aumenta y converge en aproximadamente 0,75.
En este caso, seleccionamos el valor máximo de alfa porque ejecutar el experimento para mayor los valores de alfa tienen poco impacto.
Por el contrario, a medida que aumenta el alfa, la R al cuadrado de los datos de entrenamiento disminuye. Esto es porque
el término alfa evita el sobreajuste. Esto puede mejorar los resultados en los datos invisibles, pero el modelo tiene peor desempeño en los datos de prueba. Consulte el laboratorio sobre cómo generar este diagrama.