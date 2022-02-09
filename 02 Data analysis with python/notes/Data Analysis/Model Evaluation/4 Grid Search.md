# Grid Search
La búsqueda en cuadrícula nos permite escanear múltiples parámetros libres con pocas líneas de código.
Los parámetros como el término alfa discutido en el video anterior no son parte del ajuste o proceso de formación.
Estos valores se denominan #hiperparámetros.
Scikit-learn tiene un medio de iterar automáticamente sobre estos hiperparámetros usando #ValidaciónCruzada.
Este método se llama búsqueda de cuadrícula.
La búsqueda de cuadrícula toma el modelo u objetos que le gustaría entrenar y diferentes valores de los hiperparámetros.
Luego calcula el error cuadrático medio o R cuadrado para varios valores de hiperparámetros, permitiéndole elegir los mejores valores.
Deje que los círculos pequeños representen diferentes hiperparámetros.
Comenzamos con un valor para los hiperparámetros y entrenamos el modelo.
Usamos diferentes hiperparámetros para entrenar el modelo.
Continuamos el proceso hasta que hayamos agotado los diferentes valores de los parámetros libres.
Cada modelo produce un error.
Seleccionamos el hiperparámetro que minimiza el error.
## Training, validation and test sets
Para seleccionar el hiperparámetro, dividimos nuestro conjunto de datos en tres partes, el conjunto de entrenamiento, conjunto de validación y conjunto de prueba.
Entrenamos el modelo para diferentes hiperparámetros.
Usamos el error R cuadrado o cuadrático medio para cada modelo.
Seleccionamos el hiperparámetro que minimiza el error cuadrático medio o maximiza el R al cuadrado en el conjunto de validación.
Finalmente probamos el rendimiento de nuestro modelo utilizando los datos de prueba.
Esta es la [página web](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) de scikitlearn donde se dan los parámetros del constructor del objeto.
Cabe señalar que los atributos de un objeto también se denominan parámetros.
No haremos la distinción aunque algunas de las opciones no sean hiperparámetros por decir.
En este módulo, nos centraremos en el hiperparámetro alfa y el parámetro de normalización.
El valor de su búsqueda en la cuadrícula es una lista de Python que contiene un diccionario de Python.
```py
parameters = [{'alpha':[1,10,100,100]}] 
```
La clave es el nombre del parámetro libre.
El valor del diccionario son los diferentes valores del parámetro libre.
Esto se puede ver como una tabla con varios valores de parámetros libres.
También tenemos el objeto o modelo.
La búsqueda de la cuadrícula toma el método de puntuación, en este caso R cuadrado, el número de pliegues, el modelo u objeto, y los valores de los parámetros libres.
Algunas de las salidas incluyen las diferentes puntuaciones para diferentes valores de parámetros libres;
en este caso la R al cuadrado junto con los valores de los parámetros libres que tienen la mejor puntuación.

##### Code Grid Search
```py
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

parameters1 = [{'alpha':[0.001, 0.1, 1, 10, 100, 1000, 100000]}]
RR = Ridge()
Grid1 = GridSearchCV(RR, parameters1, cv = 4)
Grid1.fit(x_data[['horesepower', 'curb_weight', 'engie.size', 'highway-mpg']], y_data)
Grid1.best_estimator_
scores = Grid1.cv_results_
scores['mean_test_score']
```
Primero, importamos las bibliotecas que necesitamos, incluido Grid Search CV, el diccionario de parámetros valores.
Creamos un objeto o modelo de regresión de cresta.
Luego creamos un objeto CV Grid Search; las entradas son el objeto de regresión de la cresta, los valores de los parámetros y el número de pliegues.
Usaremos R al cuadrado; este es el método de puntuación predeterminado.
Encajamos el objeto.
Podemos encontrar los mejores valores para los parámetros libres utilizando el mejor estimador de atributos.
También podemos obtener información como la puntuación media de los datos de validación utilizando el atributo resultado cv.
Una de las ventajas de la búsqueda en cuadrícula es la rapidez con la que podemos probar varios parámetros.

---
Por ejemplo, la regresión de Ridge tiene la opción de normalizar los datos.
```py
parameters = [{	'alpha':[1, 10, 100, 1000], 
				'normalize':[True, False] }]
```
Para ver cómo estandarizar, consulte el Módulo 4.
El término alfa es el primer elemento del diccionario, el segundo elemento es normalizar opción.
La clave es el nombre del parámetro.
El valor son las diferentes opciones, en este caso, porque podemos normalizar los datos o no, los valores son verdaderos o falsos, respectivamente.
El diccionario es una tabla o cuadrícula que contiene dos valores diferentes.
Como antes, necesitamos el objeto o modelo de regresión de cresta.
El procedimiento es similar, excepto que tenemos una tabla o cuadrícula de diferentes valores de parámetros.
La salida es la puntuación de todas las diferentes combinaciones de valores de parámetros.
El código también es similar.
```py
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

parameters2 = [{'alpha':[1, 10, 100, 1000], 
				'normalize':[True, False] }]
RR = Ridge()
Grid1 = GridSearchCV(RR, parameters2, cv = 4)
Grid1.fit(x_data[[	'horesepower', 
					'curb_weight', 
					'engie.size', 
					'highway-mpg' ]],	y_data)
Grid1.best_estimator_
scores = Grid1.cv_results_
scores['mean_test_score']
```


El diccionario contiene los diferentes valores de los parámetros libres.
Podemos encontrar el mejor valor para los parámetros gratuitos.
Las puntuaciones resultantes de los diferentes parámetros libres se almacenan en este diccionario:
`Grid1.cv_results_`
Podemos imprimir la puntuación de los diferentes valores de los parámetros libres.
Los valores de los parámetros se almacenan como se muestra aquí.
Consulte los laboratorios del curso para obtener más ejemplos.