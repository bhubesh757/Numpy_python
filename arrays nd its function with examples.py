#!/usr/bin/env python
# coding: utf-8

# #  Numpy in arrays

# In[2]:


import numpy as np


# In[3]:


help(np.array)


# In[5]:


# example 1
a= np.array([1,2,3,4])
a


# In[8]:


# 2d
np.array([[5 , 7], [9 , 8]])


# In[9]:


np.array([4 , 5 , 6] , "complex")


# In[10]:


# using tuple
np.array((4 , 5 , 6))


# # arange
# help(np.arange)
# 

# In[18]:


np.arange(5 , 15 , 2) # step


# In[19]:


np.arange(3.0) # default value for start


# In[20]:


np.arange(10 , dtype = "complex")


# In[21]:


np.arange(0 , 25 , 3 , dtype = "float")


# # zeros() what is it?

# In[ ]:


# creates array filled with zeros//


# In[23]:


import numpy as np


# In[24]:


help(np.zeros)


# In[26]:


import numpy as np


# In[27]:


np.zeros(8)   # shape


# In[28]:


np.zeros((8) , dtype = int)


# In[29]:


np.zeros((2 ,3))


# # ones() 
# create array filled with ones//

# In[30]:


import numpy as np


# In[33]:


help(np.ones)


# In[34]:


#examples
np.ones(5)


# In[36]:


np.ones((4) , dtype = "int")


# In[37]:


np.ones((5 , 3)) #rows and columns


# # empty

# In[38]:


help(np.empty)


# # linspace()  
# # linear space

# In[40]:


help(np.linspace)
# which creates the array filled evenly spaced values


# In[46]:


np.linspace(1 , 100 , num = 35)


# In[47]:


np.linspace(1 , 100 , num = 4 , endpoint = False) 


# In[48]:


np.linspace(1 , 100 , num = 4 , retstep = True) 


# In[53]:


np.linspace( 1,   10)


# In[54]:


np.linspace(9 , 10)

