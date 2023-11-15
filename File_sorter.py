#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, shutil


# In[2]:


path = r"C:/Users/Delgersaikhan/Downloads/"


# In[3]:


file_name = os.listdir(path)


# In[4]:


folder_names = ['slides', 'image', 'pdf', 'word']
for type in range(0, 4):
    if not os.path.exists(path + folder_names[type]):
        #print(path + folder_names[type])
        os.makedirs((path + folder_names[type]))
        
for file in file_name:
    if ".docx" in file and not os.path.exists(path + "word/" + file):
        shutil.move(path + file, path + "word/" + file)
    elif ".pptx" in file and not os.path.exists(path + "slides/" + file):
        shutil.move(path + file, path + "slides/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf/" + file):
        shutil.move(path + file, path + "pdf/" + file)
    elif ".png" in file and not os.path.exists(path + "image/" + file):
        shutil.move(path + file, path + "image/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image/" + file):
        shutil.move(path + file, path + "image/" + file)

