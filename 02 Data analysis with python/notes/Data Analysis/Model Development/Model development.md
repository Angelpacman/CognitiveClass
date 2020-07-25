En este Módulo, examinaremos el desarrollo del modelo tratando de ==predecir el precio== de un automóvil usando nuestro conjunto de datos

Se aprenderá sobre: 
- Regresión lineal simple y múltiple
- Evaluación del modelo mediante visualización 
- Regresión polinómica y tuberías ==pipelines==
- R-cuadrado y MSE para evaluación en muestra 
- Predicción y toma de decisiones
- ¿Y cómo se puede determinar un precio justo para un automóvil usado?

# Model
Un modelo o estimador puede considerarse como una ecuación matemática utilizada para predecir un valor siendo dados uno o más valores, relacionando una o más variables o características independientes con variables dependientes.

Por ejemplo, ingresa las millas de carretera por galón `highway-mpg` de un modelo de automóvil como variable independiente o característica, la salida del modelo o variable dependiente es el precio `predicted price`.

==Por lo general, mientras más datos relevantes tenga, más preciso será su modelo.==

Por ejemplo; ingresas múltiples variables o características independientes a tu modelo. Por lo tanto, tu modelo puede predecir un precio más preciso para el automóvil.

Para comprender por qué es importante tener más datos, considere la siguiente situación:
- Tienes dos autos casi idénticos 
- Los autos rosas se venden por mucho menos

Se desea usar tu modelo para determinar el precio de dos autos, uno rosado y uno rojo.
Si las variables o características independientes de su modelo no incluyen color, su modelo predecirá el mismo precio para autos que pueden venderse por mucho menos.
 
Además de obtener más datos, puede probar diferentes tipos de modelos. En este curso aprenderás sobre: 
- Regresión lineal simple
- Regresión lineal múltiple 
- Regresión polinómica