El método de python para quitar los datos faltantes  es `.dropna()`, por defecto tomará el df completo si no se especifica un `subset = ["nombre de la columna"]`, además se debe especificar la opción axis:

- `axis = 0` quita la ==fila== completa
- `axis = 1` quita la ==columna== completa

De forma general quitar faltantes podria verse así:
```py
df.dropna(subset = ["nombre de la columna"], axis = 0, inplace = True)
```

La opción `inplace = True` sirve para asignar los cambios al df original, es recomendable no ponerlo hasta asegurarnos de que queremos el cambio de manera definitiva

