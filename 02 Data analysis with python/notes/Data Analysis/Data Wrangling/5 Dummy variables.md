# Indicator Variable

El objetivo de las ==Dummy variables== es transformar una variable categórica en varias variables numéricas. Asumiremos que tenemos dentro de una columna una variable llamada `Combustible`:

|Combustible|
|-------------|
|gas|
|diesel|
|diesel|
|gas|
|diesel|

Convertir esta variable en indicadora nos da como resultado:

gas | diesel
----|------
1 | 0
0 | 1
0 | 1
1 | 0
0 | 1

La utilidad de estas variables es que ahora si se pueden contabilizar en un proceso y hacer uso de ellas para predicciónes de otras variables, en python se usa la función de pandas `pd.get_dummies()`

```py
dummy_variable = pd.get_dummies(df['Combustible'])
dummy_variable.rename(columns = {'gas':'combustible_gas',
								'diesel' : 'combustible_diesel', 
								inplace = True })
```

Con el código anterior es posible concatenar el resultado al df original y remover la columna original de `Combustible`