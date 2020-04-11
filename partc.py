#!/usr/bin/env python
# coding: utf-8

# In[1]:


f1 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script01.txt","r")
f2 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()
s = s1+s2
s


# In[5]:


import string
outcome1 = ''
for word in s:
        wd = word.lower()
        if wd in string.ascii_lowercase or wd == " " or wd == "\'":
            outcome1 = outcome1 + wd
        else:
            outcome1 = outcome1 + ''
outcome1 = outcome1.split()
outcome1


# In[7]:


outcome = {}
for word in outcome1:
        if word not in outcome:
            outcome[word] = 1
        else:
            outcome[word] += 1
outcome


# In[8]:


with open ("partc.txt", 'a') as f:
        for k,v in outcome.items():
            f.write(str(k) + "  " +str(v) +'\n\n')


# In[ ]:





# In[ ]:




