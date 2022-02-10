# Introduction to Matplotlib
Inicialmente matplotlib fue diseñada originalmente con una interfaz descriptiva como lo hacía matplotlib

## Arquitectura  de matplotlib:
##### Backend Layer (FigureCanvas, REnder, Event)
- _FigureCanvas:_ `matplotlib.backend_bases.FigureCanvas` (define el area en la cual la figura es dibujada)
- _Render_: `matplotlib.backend_bases.Render` (sabe como dibujar en el FigureCanvas)
- _Event_: `matplotlib.backend_bases.Event` (Handles user inputs such as keyboard strokes and mouse clicks)
##### Artist Layer (Comprende un objeto principal `Artist`)
- Sabe como usar el Renderizador para dibujar en el canvas
- Title, lines, thick labels and images, todas corresponden a instancias individuales de `Artist`
- Dos tipos de objetos `Artist`:
	- __Primitive__: Line2D, Rectange, Circle y Text
	- __Composite__: Axis, Tick, Axes y Figure
- Cada _composite_ artist puede contener _composite_ artist asi como _primitive_ artist
## Putting the Artist Layer to use
```python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas # imort FigureCanvas
from matplotlib.figure import Figure # import Figure
fig = Figure()
canvas = FigureCanvas(fig)

# create 10000 random numbers using numpy 
import numpy as np
x = np.random.randn(10000)

ax = fig.add_subplot(111) #create an axes artist

ax.hist(x, 100) #generate a histogram of the 10000 numbers

# add a title to the figure and save it
ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('matplotlib_histogram.png')
```

## Scripting Layer:
- Comprised mainly of #pyplot, a scripting interface that is lighter than the Artist layer
- Este layer fue diseñado para usar de manera mas dinamica a la hora de escribir codigo.
- Veamos como podemos generar el mismo histograma de 10000 valores aleatoreos usando la interface de #pyplot:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('matplotlib_histogram.png')
plt.show()
```

### Lectura adicional:
Puedes aprender mas de la arquitectura de #matplotlib sabiendo como fue desarrollado en el siguiente [articulo](http://aosabook.org/en/matplotlib.html)
