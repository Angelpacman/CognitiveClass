# Dataset on immigration to Canada

## Read Data into Pandas Dataframe
```python
import numpy as np # useful for many scientific computing in python
import pandas as pd # primary data structure library
from __future__ import print_function # adds compatibility to python 2
```

```python
#install xlrd in order to read some MS Excel file
!pip install xlrd

print('xlrd installed')

```

```python
filename = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx' 

df_can = pd.read_excel( filename, 
					   sheet_name="Canada by Citizenship", 
					   skiprows=range(20), 
					   skipfooter=2 )

```

## Display Dataframe
```python
df_can.head()

```


