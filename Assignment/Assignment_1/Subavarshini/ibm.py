#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[2]:


s = "Hi there Sam!"


# In[3]:


s.split( )


# *`italicized text`*## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[4]:


planet = "Earth"
diameter = 12742


# In[9]:


str = "The diameter of Earth is {} kilometers"
print(str.format(diameter))


# ## 3. In this nest dictionary grab the word "hello"

# In[10]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[11]:


d['k1'][3]['tricky'][3]['target'][3]


# # Numpy

# In[12]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[13]:


array = np.zeros(10)
print(array)


# In[14]:


array = np.ones(10)*5
print(array)


# ## 5. Create an array of all the even integers from 20 to 35

# In[15]:


array = np.arange(20,35,2)
print(array)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[16]:


array = np.arange(0,9).reshape(3,3)
print(array)


# ## 7. Concatinate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[17]:


print(np.arange('2023-01-01', '2023-02-10',
                dtype='datetime64[D]'))


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[18]:


import pandas as pd


# In[23]:


A = np.random.randint(10, size=(3,2))
print(A)


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[22]:


print(np.arange('2023-01-01', '2023-02-10',
                dtype='datetime64[D]'))


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[20]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[21]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
 
df = pd.DataFrame(lists, columns =['col1',"col2","col3"]) 
print(df)


# In[ ]:




