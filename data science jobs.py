#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/Sanchita Dabre/Desktop/EXCEL/job.csv',encoding='ANSI')
df.head()


# In[2]:


df.info()


# In[3]:


df.describe()


# In[4]:


df = df.replace(['-1'],'unknown')


# In[5]:


df['Job.Title'].unique()


# In[6]:


df['Size'].unique()


# In[7]:


df['Type.of.ownership'].unique()


# In[8]:


df['Industry'].unique()


# In[9]:


df['Job.Title'].value_counts()


# In[10]:


df.isnull().sum()


# In[11]:


df.Location.value_counts()


# In[12]:


df.Industry.value_counts()


# In[13]:


df.Industry.value_counts()


# In[14]:


get_ipython().system('pip install seaborn')
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.columns


# In[15]:


sns.pairplot(df)


# In[16]:


sns.barplot(x ='Job.Title', y ='Rating', data = df, palette ='plasma')
plt.gcf().set_size_inches(10,5)


# In[17]:


df['Industry'].value_counts().head(1000).sort_values().plot.bar(figsize = (20,6))


# In[18]:


df['Location'].value_counts().head(2000).sort_values().plot.bar(figsize = (20,6))


# In[19]:



df['Company.Name'].value_counts().head(50).sort_values().plot.bar(figsize = (20,6))


# In[20]:


df.corr()


# In[21]:


fig,ax = plt.subplots(figsize=(10, 10))   
sns.heatmap(df.corr(), ax=ax, annot=True, linewidths=0.05, fmt= '.2f',cmap="magma");


# In[ ]:




