# Overfitting underfitting and Model selection
Si recuerdas, en el último módulo discutimos la regresión polinómica.
En esta sección, discutiremos cómo elegir el mejor orden polinómico y los problemas que surgen al seleccionar el polinomio de orden incorrecto.

Considere la siguiente función: suponemos que los puntos de entrenamiento provienen de un polinomio función más algo de ruido.
$$
y(x)+noise
$$
El objetivo de la selección del modelo es determinar el orden del polinomio para proporcionar la mejor estimación de la función y x.
Si intentamos ajustar la función con una función lineal, la línea no es lo suficientemente compleja como para ajusta los datos.
Como resultado, hay muchos errores.
Esto se denomina subadaptación, donde el modelo es demasiado simple para ajustar los datos.
Si aumentamos el orden del polinomio, el modelo se ajusta mejor, pero el modelo sigue siendo no es lo suficientemente flexible y presenta un ajuste insuficiente.

Este es un ejemplo del polinomio de octavo orden utilizado para ajustar los datos; vemos el modelo hace bien para ajustar los datos y estimar la función, incluso en los puntos de inflexión.
Al aumentarlo a un polinomio de orden 16, el modelo funciona extremadamente bien en el seguimiento los puntos de entrenamiento, pero se desempeña mal al estimar la función.
==Esto es especialmente evidente cuando hay pocos datos de entrenamiento==; la función estimada oscila sin seguimiento de la función.
Esto se llama #Sobreajuste, donde el modelo es demasiado flexible y se ajusta más al ruido que la función

Veamos una gráfica del error cuadrático medio para el conjunto de entrenamiento y prueba para diferentes
ordenar polinomios.
El eje horizontal representa el orden del polinomio; el eje vertical es el error cuadrático medio.
El error de entrenamiento disminuye con el orden del polinomio.
El error de prueba es un mejor medio para estimar el error de un polinomio. El error disminuye hasta que se determine el mejor orden del polinomio, entonces el error comienza a aumentar.
Seleccionamos el orden que minimiza el error de prueba, en este caso, fue 8.
Cualquier cosa a la izquierda se consideraría inadecuada.
Cualquier cosa a la derecha es demasiado adecuada.
Si seleccionamos el mejor orden del polinomio, aún tendremos algunos errores, si recuerdas, la expresión original para los puntos de entrenamiento.Vemos un término de ruido; Este término es una de las razones del error.

Esto se debe a que el ruido es aleatorio y no podemos predecirlo; esto a veces se refiere a como ==un error irreducible==.
También hay otras fuentes de errores.
Por ejemplo, nuestra suposición polinómica puede estar equivocada.
Nuestros puntos de muestra pueden provenir de una función diferente.
Por ejemplo, en este gráfico, los datos se generan a partir de una onda sinusoidal; la función polinómica no hace un buen trabajo al ajustar la onda sinusoidal.
Para datos reales, el modelo puede ser demasiado difícil de ajustar o puede que no tengamos el tipo correcto de datos para estimar la función.
Probemos polinomios de diferente orden en los datos reales usando caballos de fuerza; los puntos rojos representan los datos de entrenamiento; Los puntos verdes representan los datos de la prueba.
Si solo usamos la media de los datos, nuestro modelo no funciona bien.
Una función lineal se ajusta mejor a los datos.
Un modelo de segundo orden es similar a la función lineal.
También parece aumentar una función de tercer orden, como las dos órdenes anteriores.
Aquí vemos un polinomio de cuarto orden.
Con alrededor de 200 caballos de fuerza, el precio previsto disminuye repentinamente; Esto parece erróneo.
Usemos R cuadrado para ver si nuestra suposición es correcta.
El siguiente es un gráfico del valor R cuadrado, el eje horizontal representa el orden de modelos polinomiales.
Cuanto más cerca esté el R cuadrado de 1, más preciso será el modelo.
Aquí vemos que el R cuadrado es óptimo cuando el orden del polinomio es tres.
El R cuadrado disminuye drásticamente cuando el orden se incrementa a 4, validando nuestra suposición inicial.

Podemos calcular diferentes valores de R cuadrado de la siguiente manera:
- Primero, creamos una lista vacía para almacenar los valores.
- Creamos una lista que contiene diferentes órdenes polinomiales.
- Luego iteramos a través de la lista usando un bucle. 
- Creamos un objeto de entidad polinómica con el orden del polinomio como parámetro 
- Transformamos los datos de entrenamiento y prueba en un polinomio usando el método de transformación de ajuste.
- Ajustamos el modelo de regresión usando el transformado datos.
- Luego calculamos el R cuadrado usando el probar datos y almacenarlos en la matriz.