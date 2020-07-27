Las gráficas de regresión son una buena estimación de:
- La relación entre dos variables,
- La fuerza de la correlación, y
- La dirección de la relación (positiva o negativa).

## Regression plot
- El eje horizontal es la variable independiente.
- El eje vertical es la variable dependiente.
- Cada punto representa un punto objetivo diferente.
- La línea ajustada representa el valor predicho.

Hay varias formas de trazar un diagrama de regresión; una manera simple es usar `.regplot()` de La biblioteca seaborn.

Primero importar seaborn.
```py
import seaborn as sns
```
Luego use la función "regplot".
```py
sns.regplot(x="highway-mpg", y="price", data = df)
plt.ylim(0,)
```
El parámetro _x_ es el nombre de la columna que contiene la variable dependiente o característica (`highway-mpg`).
El parámetro _y_ contiene el nombre de la columna que contiene el nombre de la variable dependiente o objetivo (`price`).
El parametro _data_ es el nombre del dataframe (`df`).
El resultado está dado por el diagrama:

![[sns highway-mpg-price.png]]


El gráfico residual representa el error entre los valores reales.
Examinando el valor predicho y el valor real, vemos una diferencia.
Obtenemos ese valor restando el valor predicho y el valor objetivo real.
Luego graficamos ese valor en el eje vertical, con la variable dependiente como eje horizontal.

Del mismo modo, para la segunda muestra, repetimos el proceso.
Restando el valor objetivo del valor predicho; luego trazando el valor en consecuencia.
Mirar en el diagrama nos da una idea de nuestros datos.
Esperamos ver que los resultados tengan una media igual a cero.
Distribuido uniformemente alrededor del eje x con una varianza similar; no hay curvatura.
Este tipo de gráfico residual sugiere que un gráfico lineal es apropiado.

---
En esta gráfica residual hay curvatura, los valores del error cambian con x.
Por ejemplo, en la región, todos los errores residuales son positivos.
En esta área, los residuos son negativos.
En la ubicación final, el error es grande.
Los residuos no están separados al azar; Esto sugiere que la suposición lineal es incorrecta.
Este gráfico sugiere una función no lineal, trataremos esto en la siguiente sección.
En este gráfico, vemos que la varianza de los residuos aumenta con x, por lo tanto, nuestro modelo es incorrecto.

## Residual plot
Podemos usar ==seaborn para crear un residual Plot==.
- Primero importamos seaborn
```py
# primero importamos seaborn
import seaborn as sns
```
- Luego usamos la función `.residplot()`
```py
sns.residplot(df['highway-mpg'], df['price'])
```
![[Residual highway-mpg.png]]

El primer parámetro es una serie de variable o característica dependiente.
El segundo parámetro es una serie de variable dependiente u objetivo.
Vemos en este caso los Residuos tienen una curvatura.

## Distribution plot
==Un diagrama de distribución cuenta el valor predicho vs al valor real==.
Estas gráficas son extremadamente útiles para visualizar modelos con más de una variable independiente o característica.
Veamos un ejemplo simplificado: 
- Examinamos el eje vertical.
- Luego contamos y graficamos el número de puntos predichos que son aproximadamente iguales a uno.
- Luego contamos y graficamos el número de puntos predichos que son aproximadamente iguales a dos.
- Repetimos el proceso para los puntos pronosticados que son aproximadamente iguales a tres.
Luego repetimos el proceso para los valores objetivo.
En este caso, todos los valores objetivo son aproximadamente iguales a dos.
Los valores de los objetivos y los valores pronosticados son continuos.
Un histograma es para valores discretos.
Por lo tanto, los pandas los convertirán en una distribución.
El acceso vertical se escala para hacer que el área bajo la distribución sea igual a uno.
Este es un ejemplo del uso de un diagrama de distribución.
La variable o característica dependiente es el precio.
Los valores ajustados que resultan del modelo están en azul.
Los valores reales están en rojo.
Vemos que los valores pronosticados para los precios en el rango de 40 000 a 50 000 son inexactos.
Los precios en la región de 10 000 a 20 000 están mucho más cerca del valor objetivo.

## MRL ditribution plots
En este ejemplo, usamos múltiples características o variables independientes.
Comparándolo con el gráfico de la última diapositiva, vemos que los valores pronosticados están mucho más cerca de
los valores objetivo


## Distribution plot
Aquí está el código para crear un diagrama de distribución.
```py
# primero hacemos la predicción
Y_hat = lm.predict(Z)
# luego armamos la figura
plt.figure(figsize=(width, height))
# valores reales
ax1 = sns.distplot(	df['price'], 
					hist=False,
					color="r",
					label="Actual Value" )
# valores predictivos
sns.distplot(Yhat,
			hist=False, 
			color="b", 
			label="Fitted Values" ,
			ax=ax1	)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
plt.show()
plt.close()
```
![[Distribution plot.png]]
Los valores reales se utilizan como parámetro.
Queremos una distribución en lugar de un histograma, por lo que queremos que el parámetro `hist` se establezca en `False`.
El color es rojo.
La etiqueta también está incluida.
Los valores predichos se incluyen para el segundo gráfico; el resto de los parámetros son establecidos en consecuencia.


[[3 Polynomial regression & Pipelines | Regresión polinominal y Pipelines]]