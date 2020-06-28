#!/usr/bin/env python
# coding: utf-8

# You will need the class Car for the next exercises. The class Car has four data attributes: make, model, colour and number of owners (owner_number). The method <code> car_info() </code>  prints out the data attributes and the method <code>sell()</code> increments the number of owners. 

# In[5]:


class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1


# <h3> Create a Car object </h3>

# Create a <code> Car </code> object my_car with the given data attributes: 

# In[10]:


make="BMW"
model="M3"
color="red"
my_car = Car(make,model,color)


# <h3> Data Attributes </h3>

# Use the method car_info() to print out the data attributes

# In[12]:


my_car.car_info()


# <h3> Methods  </h3>

# Call the method <code> sell() </code> in the loop, then call the method <code> car_info()</code> again 

# In[ ]:


for i in range(5):
    


# <hr>
# <small>Copyright &copy; 2018 IBM Cognitive Class. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/).</small>
