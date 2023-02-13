#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats


# In[5]:


#рост больше 182
a= 1- stats.norm.cdf(182, loc = 174, scale = 8)
print(a)


# In[15]:


#рост больше 190
b =stats.norm.cdf(190, loc = 174, scale = 8)
b1 = 1-b
print(b1)


# In[7]:


#рост меньше 166
c=stats.norm.cdf(166, loc = 174, scale = 8)
print(c)


# In[8]:


#рост меньше 158
d=stats.norm.cdf(158, loc = 174, scale = 8)
print(d)


# In[16]:


#рост от 166 до 190
print(b-c)


# In[17]:


#рост от 166 до 182
print(stats.norm.cdf(182, loc = 174, scale = 8)-c)


# In[ ]:




