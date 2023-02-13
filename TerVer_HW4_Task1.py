#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats


# In[2]:


# fill array
arr=[]
num1=200
num2=800
for i in range(num1, num2):
    num1 = num1+1
    arr.append(num1)
print(arr)


# In[5]:


x=np.array(arr)


# In[8]:


# находим дисперсию (по умолчанию смещенная, поэтому добвляем необязательный элемент, чтобы найти несмещенную)
x.var(ddof=1)


# In[7]:


# находим среднее арифмеетическое
x.mean()


# In[ ]:




