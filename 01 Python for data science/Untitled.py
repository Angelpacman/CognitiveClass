#!/usr/bin/env python
# coding: utf-8

# In[1]:


a =[3,6,8,4,6,9,5,9,4]
a


# In[2]:


a.sort()
print(a)


# In[5]:


import pandas as banana

df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})

df.head()


# In[6]:


type(df)


# In[8]:


import pandas as pd


# In[9]:


df1=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
df1.head()


# In[10]:


df['a']==1


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


a=np.array([0,1,0,1,0])

b=np.array([1,0,1,0,1])

a*b


# In[3]:


a=np.array([0,1])

b=np.array([1,0])

np.dot(a,b)


# In[4]:


a=np.array([1,1,1,1,1])

a+10


# In[6]:


A='1234567'
A[1::2]


# In[7]:


A='1'
B='2'
A+B


# In[8]:


A=((11,12),[21,22])
A[1]


# In[9]:


'1,2,3,4'.split(',')


# In[10]:


A=[1,'a']
B=[2,1,'d']
A+B


# In[14]:


a = set(A)
a


# In[16]:


a.add('C')
a


# In[18]:


x="Go"

if(x!="Go"):

    print('Stop')

else:

    print('Go ')

print('Mike')


# In[19]:


x="Go"

if(x=="Go"):

    print('Go ')

else:

    print('Stop')

print('Mike')


# In[21]:


for n in range(3):

    print(n)


# In[23]:


def Add(x,y):

    z=y+x

    return(y)

Add('1','1')


# In[24]:


class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def print_point(self):

        print('x=',self.x,' y=',self.y)

p1=Points(1,2)

p1.print_point()


# In[25]:


class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def print_point(self):

        print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=2

p2.print_point()


# In[ ]:




