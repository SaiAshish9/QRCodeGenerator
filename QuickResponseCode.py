#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrcode


# In[2]:


qr=qrcode.make('hello world')


# In[3]:


qr.save('qr.png')


# In[4]:


from IPython.display import Image


# In[5]:


Image(filename='qr.png')


# In[37]:


qr=qrcode.QRCode(
version=1,
# error_correction=qrcode.ERROR_CORRECT_M
box_size=3,
border=5
)


# In[38]:


data='https://www.google.com'


# In[39]:


qr.add_data(data)


# In[40]:


qr.make(fit=True)


# In[46]:


img=qr.make_image(fill_color='red',back_color='white')


# In[47]:


img.save('qr1.png')


# In[48]:


Image(filename='qr1.png')


# In[ ]:




