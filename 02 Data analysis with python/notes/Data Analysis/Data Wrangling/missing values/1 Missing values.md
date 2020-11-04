# Lidiar con valores faltantes en Python
 Cuando no se almacena ningun valor de datos para alguna caracteristica (==feature==) para alguna observación en particular, decimos que esta caracteristica tiene un valor faltante.
 
 Ejemplos de *missing values*: `N/A, 0, espacios en blanco " "`

Cada forma de lidiar con estos valores es diferente, y dependerá de factores como el propósito del análisis, la relacion de faltantes y el numero total de observaciones, el tipo de objeto al que debería pertenecer. Cada situación se juzga de diferente marera.

---
## Opciones a considerar:
-  La primera opción es verificar si es posible contactar al grupo de personas que recolectaron los datos y llenar los faltantes.
-  Si lo anterior no fue posible entonces se puede considerar [[Remover faltantes]], remover el dato (observación) que falta se puede hacer quitando la variable en que se encuentra(==quitando toda la columna==) o quitando la entrada en la que se encuentra(==quitando toda la fila==). El criterio para eliminar datos faltantes se basa en buscar la forma que tenga el menor impacato al df.
-  [[Remplazar faltantes]] :

Valores numéricos | Valores categóricos
-------------------|----------------------
Cuando los valores faltantes deberian ser *numeros* entonces se pueden remplazar con el valor promedio de la variable | Si los faltantes son categóricos  se puede intentar intuir cual es la categoria en la columna y asi llenar el vacio si es que el remplazo tiene sentido

- Por último esta la opción de considerar dejar los datos faltantes tal y como están  y usar el dataframe con precauciones necesarias a la hora da hacer el análisis.