#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import strftime, localtime


# In[2]:


# 打印当前时间
def printTime():
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    return

