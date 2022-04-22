# Scatterplots

A `scatter plot` (2D) is a useful method of comparing variables against each other. `Scatter` plots look similar to `line plots` in that they both map independent and dependent variables on a 2D graph. While the data points are connected together by a line in a line plot, they are not connected in a scatter plot. The data in a scatter plot is considered to express a trend. With further analysis using tools like regression, we can mathematically calculate this relationship and use it to predict trends outside the dataset.

Let's start by exploring the following:

Using a `scatter plot`, let's visualize the trend of total immigrantion to Canada (all countries combined) for the years 1980 - 2013.

Step 1: Get the dataset. Since we are expecting to use the relationship betewen `years` and `total population`, we will convert `years` to `int` type.

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

df_total.plot(
			  kind='scatter',
			  x='year',
			  y='total'
)

plt.title('Total Immigrant population to Canada from 1980-2013')
plt.xlabel('Year')
plt.ylabel('Numer of immigrants')

plt.show()
```