#!/usr/bin/env python
# coding: utf-8

# <h3> Get to Know a numpy Array </h3>

# You will use the numpy array <code> A</code> for the following 

# In[6]:


import numpy as np
A=np.array([[11,12],[21,22],[31,32]])


# 1) type using the function type 

# In[ ]:





# 2) the shape of the array 

# In[ ]:





# 3) the type of data in the array 

# In[ ]:





# 4) Find the second row of the numpy array <code>A</code>:

# In[ ]:





# <h3> Two kinds of Multiplying  </h3>

# you will use the following numpy arrays for the next questions 

# In[8]:


A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])


# 1) multiply array <code> A </code> and <code>B</code>

# 

# In[10]:


A*B


# 2)  plot the function

# In[12]:


np.dot(A,B)
np.dot(B,A)


# <hr>
# <small>Copyright &copy; 2018 IBM Cognitive Class. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/).</small>
