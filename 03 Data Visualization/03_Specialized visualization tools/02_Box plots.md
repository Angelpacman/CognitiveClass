
# Box Plots

A `box plot` is a way of statistically representing the _distribution_ of the data through five main dimensions:

-   **Minimum:** The smallest number in the dataset excluding the outliers.
-   **First quartile:** Middle number between the `minimum` and the `median`.
-   **Second quartile (Median):** Middle number of the (sorted) dataset.
-   **Third quartile:** Middle number between `median` and `maximum`.
-   **Maximum:** The largest number in the dataset excluding the outliers.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%203/images/boxplot_complete.png)

Let's plot the box plot for the Japanese immigrants between 1980 - 2013.

Step 1: Get the subset of the dataset. Even though we are extracting the data for just one country, we will obtain it as a dataframe. This will help us with calling the `dataframe.describe()` method to view the percentiles.

Step 2: Plot by passing in `kind='box'`.

```python
import matplotlib.pyplot as plt
import matplotlib as mpl


df_japan = df_canada.loc[['Japan'], years].transpose()

df_japan.plot(kind='box')

plt.title('Box plot of Japanese Immigrations from 1980-2013')
plt.show()
```

We can view the actual numbers by calling the `describe()` method on the dataframe.

	df_japan.describe()


## Outliers
Note how the box plot differs from the summary table created. The box plot scans the data and identifies the outliers. In order to be an outlier, the data value must be:  

>-   #larger than Q3 by at least 1.5 times the interquartile range (IQR), or,
>-   #smaller than Q1 by at least 1.5 times the IQR.


Let's look at decade 2000s as an example:  

-   Q1 (25%) = 36,101.5  
-   Q3 (75%) = 105,505.5  
-   IQR = Q3 - Q1 = 69,404  
    

Using the definition of outlier, any value that is greater than Q3 by 1.5 times IQR will be flagged as outlier.

Outlier > 105,505.5 + (1.5 * 69,404)  
Outlier > 209,611.5