Hablaremos sobre la correlación entre diferentes variables. La correlación es una métrica estadística para medir hasta qué punto las diferentes variables son interdependientes. En otras palabras, cuando miramos dos variables a lo largo del tiempo, si una variable cambia, ¿cómo afecta esto al cambio en la otra variable?

Por ejemplo, se sabe que fumar está relacionado con el cáncer de pulmón.
Dado que tiene una mayor probabilidad de contraer cáncer de pulmón si fuma.
En otro ejemplo, existe una correlación entre paraguas y variables de lluvia donde más precipitación significa que más personas usan paraguas.
Además, si no llueve, las personas no llevarían paraguas.
Por lo tanto, podemos decir que los paraguas y la lluvia son interdependientes y, por definición, están correlacionados.

==Es importante saber que la correlación no implica causalidad==.
De hecho, podemos decir que el paraguas y la lluvia están correlacionados, pero no tendríamos suficiente información para decir si el paraguas causó la lluvia o la lluvia causó el paraguas.
En ciencia de datos, generalmente tratamos más con la correlación.

### Relación lineal positiva
Veamos la correlación entre el `engine-size` y `price`.

```py
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
```
![[scatter-Enginesize-price.png]]

Esta vez visualizaremos estas dos variables usando un diagrama de dispersión y una línea lineal agregada llamada línea de regresión, que indica la relación entre los dos.

El objetivo principal de este diagrama es ver si el `engine-size` tiene algún impacto en el `price`.
En este ejemplo, puede ver que la línea recta a través de los puntos de datos es muy empinado y que muestra que hay una relación lineal positiva entre las dos variables.
Con el aumento en los valores del `engine-size`, los valores del `price` también suben y la pendiente de la línea es positiva. Por lo tanto, existe una correlación positiva entre el `engine-size` y el `price`.

Podemos usar `seaborn.regplot()` para crear el diagrama de dispersión.

### Relación lineal negativa
Como otro ejemplo, ahora veamos la relación entre millas de carretera por galón `highway-mpg` para ver su impacto en el `price` del automóvil.
```py
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
```

![[scatter-highway-mpg-price.png]]

Como podemos ver en este diagrama, cuando el valor de millas por galón en carretera sube, el `price` del valor baja. Por lo tanto, hay una relación lineal negativa entre millas de carretera por galón `highway-mpg` y `price`.
Aunque esta relación es negativa, la pendiente de la línea es empinada
lo que significa que las millas de autopista por galón siguen siendo un buen indicador del `price`.
Se dice que estas dos variables tienen una correlación negativa.

### Relación lineal debil
```py
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
```
![[scatter-peak-rpm-price.png]]

Finalmente, tenemos un ejemplo de una correlación débil.
Por ejemplo, tanto RPM pico bajo como valores altos de RPM pico tienen `price`s bajos y altos.
Por lo tanto, no podemos usar RPM para predecir los valores.
