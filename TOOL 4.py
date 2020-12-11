#!/usr/bin/env python
# coding: utf-8

# In[43]:


#Import Everything
import matplotlib as plt
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import random
import pymysql


# In[13]:


youtube = pd.read_excel (r'C:\Users\Username\Downloads\youtube_dataset.xlsx')
youtube.head(1000)


# In[33]:


#Define table
def my_function(x):
    empty_list = x[0:1000] 
    return empty_list['channeltype'].value_counts()


# In[34]:


my_function(df)


# In[38]:


raw_df = df.iloc[0:1000]
print(raw_df)


# In[44]:


engine = create_engine('mysql+pymysql://Username:Password@localhost/vg_db')
# connection string
conn = engine.connect()


# In[45]:


raw_df.to_sql(con = conn,name = 'youtube')


# In[ ]:




