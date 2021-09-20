#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#height in float 
height = float(input("Height(m): "))


# In[ ]:


#weight in float 
weight = float(input("Weight(kg): "))


# In[ ]:


#calculating the body mass index 
bmi = (weight) / (height * height) 
print(f"Body Mass Index is {round(bmi,3)}")


# In[ ]:




