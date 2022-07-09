#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # creat data points

# In[3]:


df = pd.DataFrame(columns=['x', 'y'])


# In[9]:


df.loc[0] = [3,1]
df.loc[1] = [4,1]
df.loc[2] = [3,2]
df.loc[3] = [4,2]
df.loc[4] = [10,5]
df.loc[5] = [10,6]
df.loc[6] = [11,5]
df.loc[7] = [11,6]
df.loc[8] = [15,1]
df.loc[9] = [15,2]
df.loc[10] = [16,1]
df.loc[11] = [16,2]


# In[5]:


df.head(20)


# # Visualize data points on 2D plot

# In[17]:


# visualize data point
sns.lmplot('x', 'y', data=df, fit_reg=False, scatter_kws={"s":200}) # x-axis, y-axis, data, no line, marker size

# title
plt.title('kmean plot')

# x-axis label
plt.xlabel('x')

# y-axis label
plt.ylabel('y')


# # k-mean clustering

# In[11]:


# convert dataframe to numpy array
data_points = df.values


# In[12]:


kmeans =  KMeans(n_clusters=3).fit(data_points)


# In[13]:


# cluster id for each data point
kmeans.labels_


# In[14]:


# this is final centroids position
kmeans.cluster_centers_


# In[15]:


df['cluster_id'] = kmeans.labels_


# In[16]:


df.head(12)


# In[18]:


sns.lmplot('x', 'y', data=df, fit_reg=False, # x-axis, y-axis, data, no line)
           scatter_kws={"s": 150}, # marker size
           hue="cluster_id") # color
# title
plt.title('after kmean clustering')


# In[ ]:




