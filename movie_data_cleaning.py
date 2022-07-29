#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#importing pandas library as pd
import pandas as pd
#reading the excel sheet to python
dataset = pd.read_excel("Movies_Database.xlsx")
#showing the content in dataset
dataset
#showing first 5 rows of the dataset
dataset.head()
#check the tail:
dataset.tail(5)
#showing the column header
dataset.columns
dataset.index
dataset.values
type(dataset)
dataset.shape


# In[2]:


dataset.info()


# In[3]:


dataset['movie_title']


# In[4]:


dataset['movie_title'] = dataset['movie_title'].str.replace(r'[?ÿ]',"")
print(dataset)


# In[5]:


dataset


# In[6]:


dataset.info()


# In[7]:


dataset.shape


# In[8]:


pd.isnull(np.nan)


# In[9]:


pd.isnull(dataset)


# In[10]:


dataset.isnull().sum()


# In[11]:


#filling notnull values with 0
dataset.fillna(0)


# In[12]:


dataset.info()


# In[13]:


dataset['DIRECTOR_facebook_likes'][4] =int(dataset['DIRECTOR_facebook_likes'][4].replace('"',''))


# In[14]:


type(dataset['DIRECTOR_facebook_likes'][1])


# In[15]:


dataset.fillna(0)


# In[16]:


dataset.info()


# In[17]:


dataset['DIRECTOR_facebook_likes'] = dataset['DIRECTOR_facebook_likes'].fillna(0).astype(int)


# In[18]:


dataset.info()


# In[19]:


dataset = dataset.fillna(0)


# In[20]:


dataset.info()


# In[ ]:




