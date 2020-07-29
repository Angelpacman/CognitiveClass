# Correlación Avanzada
Aquí, le presentaremos varios métodos estadísticos de correlaciones.
Una forma de medir la fuerza de la correlación entre las variables numéricas continuas es mediante el uso de un método llamado ==correlación de Pearson==.
El método de correlación de Pearson le dará dos valores: 
- El coeficiente de correlación
- El valor P. 

Entonces, ¿cómo interpretamos estos valores?

## Coeficiente de correlación 
Para el coeficiente de correlación: 
- un valor cercano a +1 implica una gran correlación positiva
- un valor cercano a -1 implica una gran correlación negativa
- un valor cercano a 0 implica que no hay correlación entre las variables.

## P-value
¿Qué es este valor P? El valor P es el valor de probabilidad de que la correlación entre estas dos variables sea estadísticamente significativa. Normalmente, elegimos un nivel de significancia de 0.05, lo que significa que estamos 95% seguros de que la correlación entre las variables es significativa.

A continuación, el valor P nos dirá cómo estamos seguros de la correlación que calculamos:

- el valor p < 0.001: decimos que existe una ==fuerte== evidencia de que la correlación es significativa.
- el valor p < 0.05: existe evidencia ==moderada== de que la correlación es significativa.
- el valor p < 0.1: existe evidencia ==débil== de que la correlación es significativa.
- el valor p > 0.1: ==no hay== evidencia de que la correlación sea significativa.

Podemos decir que ==hay una fuerte correlación cuando el coeficiente de correlación es cercano a +1 o -1, y el valor P es menor que 0.001==

La siguiente gráfica muestra datos con diferentes valores de correlación.
![[correlation.png]]

En este ejemplo, queremos ver la correlación entre la potencia `horsepower` y el precio `price` del automóvil usando el método `stats.pearsonr()`.

```py
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
```
	The Pearson Correlation Coefficient is 0.584641822265508  with a P-value of P = 8.076488270733218e-20

¿Ves lo fácil que puedes calcular la correlación de Pearson usando el paquete de estadísticas SI / PI?
Podemos ver que el coeficiente de correlación es aproximadamente 8, y esto está cerca de 1. Entonces hay una fuerte correlación positiva. También podemos ver que el valor P es muy pequeño, mucho más pequeño que 001.
Y así podemos concluir que estamos seguros de la fuerte correlación positiva.

Teniendo en cuenta todas las variables, ahora podemos crear un mapa de calor que indica la correlación entre cada una de las variables entre sí.
![[correlation_heatmap.png]]
El esquema de color indica el coeficiente de correlación de Pearson, indicando la fuerza de la correlación entre dos variables.
Podemos ver una línea diagonal con un color rojo oscuro, indicando que todos los valores en esta diagonal están altamente correlacionados.
Esto tiene sentido porque cuando miras más de cerca, los valores en la diagonal son la correlación de todas las variables consigo mismas, que siempre será 1.

Este mapa de calor de correlación nos da una buena visión general de cómo las diferentes variables están relacionadas entre sí y, lo más importante, cómo estas variables están relacionadas con el precio `price`.