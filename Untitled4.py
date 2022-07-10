#!/usr/bin/env python
# coding: utf-8

# # Jupiter Tutorial
# ## 1. What is Jupyter Notebook?

# The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualization.

# ## 2. Live Code Example

# In[3]:


3+4


# In[4]:


# adding two parameter
def add(a,b):
    return a+b


# In[5]:


add(5,4)


# ## 3. Equation

# In[6]:


#sqrt(x^2+y^2+z^2)


# This expression $\sqrt{x^2+y^2+z^2}$ is an example of a TeX inline equation

# [More Examples click here](http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html)

# ## 4. Visualization

# ### 4.1 image

# In[5]:


from IPython.display import Image
Image(url = "https://images.velog.io/images/t1won/post/bfae116b-aa6b-4831-b2d2-8395193361cf/jupyter.png", width=400, height=200)


# ### 4.2 video

# In[23]:


from IPython.display import YouTubeVideo
YouTubeVideo('vJwrhhL5f8Y')


# ### 4.3 table

# In[37]:


import pandas as pd
url ="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
pd.read_csv(url, nrows=10)


# ### 4.4 chart

# In[38]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('result')
plt.show()


# ## 5. Performance check

# In[9]:


get_ipython().run_line_magic('timeit', '3+4')


# In[10]:


get_ipython().run_line_magic('timeit', 'add(3,4)')


# In[43]:


get_ipython().run_cell_magic('timeit', '', 'a = [1,2,3]\na = [x+1 for x in a]')


# In[42]:


get_ipython().run_cell_magic('timeit', '', 'b = [1,2,3]\nfor i in range(len(b)):\n    b[i] = b[i] + 1')

