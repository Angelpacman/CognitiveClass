# Basic plotting with matplotlib
Matplotlib puede ser usado en un script de python, una notebook de jupyter, o una gui.

## Plot function
Cuando se realiza un grafico dentro de jupyter notebook se utiliza matplotlib como una #MagicFunction que significa que la figura será vista desde dentro del navegador en el que está corriendo la jupyter notebook

```python
%matplotlib notebook
import matplotlib.pyplot as plt
plt.plot(5,5,'O')
```
Con la notebook backend inplace,  si una funcion plt es llamada entonces verifica si existe alguna figura activa, cualquier funcion que llamemos se aplicará a la figura que ya existe, en caso de que no exista el programa va a renderizar una nueva figura
## Matplotlib with pandas
Si tenemos und DataFame de pandas podemos llamar directamente al metodo `.plot()` y pasarle como argumento el tipo de gráfico que queremos desplegar por ejemplo `kind="histo"`

```python
import pandas as pd

india_china_df = read.csv("some_file.csv")

india_china_df.plot(kind="histo")

```
