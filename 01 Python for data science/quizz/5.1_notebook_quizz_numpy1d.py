#!/usr/bin/env python
# coding: utf-8

# <h3> Get to Know a numpy Array </h3>

# cast the following list to a numpy array:

# In[ ]:


import numpy as np
a=[1,2,3,4,5]


# 1) type using the function type 

# In[ ]:





# 2) the shape of the array 

# In[ ]:





# 3) the type of data in the array 

# In[ ]:





# 4) find the mean of the array 

# In[ ]:





# <h3> Creating and Plotting Functions  </h3>

# 1) create the following functions using the numpy array <code> x </code>

# $$y=sin(x)+2$$

# In[ ]:


x=np.linspace(0,2*np.pi,100)


# 2)  plot the function

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')



# <hr>
# <small>Copyright &copy; 2018 IBM Cognitive Class. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/).</small>
