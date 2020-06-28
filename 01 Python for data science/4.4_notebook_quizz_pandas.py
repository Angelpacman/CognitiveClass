#!/usr/bin/env python
# coding: utf-8

# <h3> Get to Know a Pandas Array </h3>

# You will use the dataframe <code>df</code> for the following:

# In[1]:


import pandas as pd

df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})


# 1) find the unique values in column <code> 'a' </code>:

# In[3]:


df['a'].unique()


# 2) return a dataframe with only the rows where column <code> a </code> is less than two 

# In[ ]:


df[df['a']]


# <hr>
# <small>Copyright &copy; 2018 IBM Cognitive Class. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/).</small>
