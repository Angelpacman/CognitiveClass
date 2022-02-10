# Bar chart
A diferencia del histograma, un bar chart es comunmente usado para comparar el valor de una variable a un punto dado en el tiempo _"se usa una linea de tiempo"_.

```python 
import matplotlib as mpl
import matplotlib.pyplot as plt
```

```python
years = list(map(str, range(1980 2014)))

df_iceland = df_canada.loc['Iceland', years]
```

```python
df_iceland.plot(kind='bar')

plt.title('Icelandic immigrants to Canada from 1980 to 2013')
plt.xlabel('Year')
plt.ylabel('Numer of immigrants')

plt.show()
```

