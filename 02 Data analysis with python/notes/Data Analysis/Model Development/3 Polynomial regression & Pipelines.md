# Polynomial regression and Pipelines
¿Qué hacemos cuando un modelo lineal no es el mejor para nuestros datos?
Veamos otro tipo de modelo de regresión: la regresión polinómica.
Transformamos nuestros datos en un polinomio, luego usamos regresión lineal para ajustar el parámetro.
Luego discutiremos las tuberías.
Las tuberías son una forma de simplificar su código.
## Regresión polinómica
- ==La regresión polinómica es un caso especial de la regresión lineal general.==
- Este método es beneficioso para ==describir las relaciones curvilíneas.==
![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Polyreg_scheffe.svg/325px-Polyreg_scheffe.svg.png)
## ¿Qué es una relación curvilínea?
Es lo que obtienes al cuadrar o establecer términos de orden superior de las variables predictoras en el modelo, transformando los datos.
El modelo puede ser cuadrático, lo que significa que la variable predictora en el modelo es cuadrada.

$\hat{Y}=b_{0}+b_{1}x_{1}+b_{2}(x_{1})^2$

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeIdCVbxTL21iGM-tc9lkjxZrgd_l0mWnIeg&usqp=CAU)

Usamos un paréntesis para indicar que es un exponente.
Esta es una regresión polinómica de segundo orden con una figura que representa la función.

El modelo puede ser cúbico, lo que significa que la variable predictora está en cubos.

$\hat{Y}=b_{0}+b_{1}x_{1}+b_{2}(x_{1})^2+b_{3}(x_1)^3$

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdxpyeBJJXLbzuSgWJ-ZDm2bjjpk-WzzDmHw&usqp=CAU)

Esta es una regresión polinómica de tercer orden.
Al examinar la figura, vemos que la función tiene más variación.

También existen regresiones polinómicas de orden superior, cuando un buen ajuste no ha sido logrado por segundo o tercer orden.

Podemos ver en las figuras cuánto cambian las gráficas cuando cambiamos el orden del polinomio regresión.

$\hat{Y}=b_{0}+b_{1}x_{1}+b_{2}(x_{1})^2+b_{3}(x_1)^3+...$
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPcYoR7dnnnDHlSiOnoODI1oT3Pq_hY6hylw&usqp=CAU)

==El grado de la regresión hace una gran diferencia y puede resultar en un mejor ajuste si elige el valor correcto.==
En todos los casos, la relación entre la variable y el parámetro siempre es lineal.
Veamos un ejemplo de nuestros datos donde generamos un modelo de regresión polinómica.

En Python, hacemos esto usando la función `.polyfit()` que pertenece a numpy.
En este ejemplo, desarrollamos una base de modelo de regresión polinómica de tercer orden.
```py
f = np.polyfit(x,y, 3)
p = np.poly1d(f)
# podemos imprimir el modelo
print(p)
#-1.557 x³ + 204.8 x² - 8965 x + 1.379e+05
```
La forma simbólica para el modelo viene dada por la siguiente expresión $$-1.557 (x_1) ^3 + 204.8 (x_1) ^2 + 8965 x_1 + 1.37 * 10^5$$

## Regresión polinómica con mas de una Dimensión
También podemos tener regresión lineal polinómica multidimensional.
La expresión puede complicarse; Estos son solo algunos de los términos para un polinomio bidimensional de segundo orden.

La función `.polyfit()` de Numpy no puede realizar este tipo de regresión.
Usamos la biblioteca `preprocessing` en _scikit-learn_, para crear un objeto polinomial.
```py
from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degreee = 2, include_bias = False)
x_polly = pr.fit_transform(x[['horsepower', 'curb-weight']])
```
El constructor toma el grado del polinomio como parámetro.
Luego transformamos las entidades en una entidad polinómica con el método `fit_transform`.

## Polinomial Regression with more than One Dimension
Hagamos un ejemplo más intuitivo.
Considere las características que se muestran aquí.
Aplicando el método, transformamos los datos. Ahora tenemos un nuevo conjunto de características que son
Una versión transformada de nuestras características originales.

### Pre-procesamiento
A medida que aumenta la dimensión de los datos, es posible que deseemos normalizar varias funciones en scikit-learn, en cambio, podemos usar el módulo de preprocesamiento para simplificar muchas tareas.
Por ejemplo, podemos estandarizar cada característica simultáneamente.
- Importamos `StandardScaler` 
- Entrenamos el objeto
- Ajustamos el objeto de escala;
- Luego transforme los datos en un nuevo data frame en la matriz `x_scale`.
```py
from sklearn.preprocessing import StandardScaler
SCALE = StandardScaler()
SCALE.fit(x_data[['horsepower', 'highway-mpg']])
x_scale = SCALE.transform(x_data[['horsepower', 'highway-mpg']])
```
Hay más métodos de normalización disponibles en la biblioteca de preprocesamiento, así como otras transformaciones.

## Pipelines
Podemos simplificar nuestro código utilizando una biblioteca de `pipeline()`.
Hay muchos pasos para obtener una predicción, por ejemplo:
- Normalización, 
- Transformación polinómica,
- Regresión lineal.

Simplificamos el proceso usando una tubería.
Las tuberías realizan secuencialmente una serie de transformaciones.
El último paso lleva a cabo una predicción.
Primero importamos todos los módulos que necesitamos.
```py
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
```
Luego importamos la biblioteca Pipeline.
```py
from sklearn.pipeline import Pipeline
```
Creamos una lista de tuplas, el primer elemento de la tupla contiene el nombre del estimador: modelo.
```py
Input=[ ('scale', StandardScaler()), 
		('polynomial', PolynomialFeatures(include_bias=False)), 
		('model',LinearRegression()) ]
```
El segundo elemento contiene el constructor del modelo.
Ingresamos la lista en el constructor de tuberías.
```py
Pipe = Pipeline(Input)
```
Ahora tenemos un objeto de pipeline.
Podemos entrenar la tubería aplicando el método de entrenamiento al objeto Pipeline.
```py
Pipe.train(X['horsepower', 
			'curb-weight', 
			'engine-size', 
			'highway-mpg'], y)
```
También podemos producir una predicción también.
```py
yhat = Pipe.predict(X[ ['horsepower', 
						'curb-weight', 
						'engine-size', 
						'highway-mpg'] ])
```
El método normaliza los datos, realiza una transformación polinómica y luego genera una predicción.

[[4 Measures for In-Sample Evaluation]]