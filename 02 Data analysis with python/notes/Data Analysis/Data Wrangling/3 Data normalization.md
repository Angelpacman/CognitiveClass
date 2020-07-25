Normalizar los datos es el proceso de transformar los valores de varias variables en rangos similares.

La justificación de este proceso viene del hacho de que si se usan 2 variables en una regresion lineal pero una de las variables tiene rangos de valores significativamente mayores que la otra variable, entonces va a infuir intrinsecamente en mas en el resutado que la variable con rangos menores.

##### Métodos de normalización de datos
Modelo | Fórmula | Descripción 
--------|--------------|---------
Simple feature scaling | $x_{new} = \frac{x_{old}}{x_{max}}$ | Hace que los nuevos valores oscilen entre 0 y 1
Min-Max | $x_{new} = \frac {x_{old} - x_{min}}  {x_{max} - x_{min}}$ | Sus rangos tambien van de 0 a 1
z-score | $x_{nex} = \frac {x_{old} - \mu} {\sigma}$ | Tambien se le conoce como ==standard score==, los valores ronda cerca de 0 y tipicamente van de -3 a +3 pero el rango puede ser mayor o menor

---
Métodos útiles para normalizar en python:

Método | Variable | Descripción
-------|---------|---------
`.min()` | $x_{min}$ | Valor minimo de x
`.max()` | $x_{max}$ | Valor máximo de x
`.mean()` | $\mu$ | Valor promedio de una muestra (en este caso x)
`.std()` | $\sigma$ | Desviación estandar de una muestra (tomamos a x como la muestra)
