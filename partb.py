#!/usr/bin/env python
# coding: utf-8

# In[7]:


import operator
f1 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script01.txt","r")
f2 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()
s = s1+s2
s


# In[8]:


atoz = "abcdefghijklmnopqrstuvwxyz"
outcome ={}
for character in s:
    ch = character.lower()
    if ch in atoz:
        if ch not in outcome:
            outcome[ch] = 1
        else:
            outcome[ch] += 1
outcome


# In[9]:


with open ("partb.txt", 'a') as f:
        for k,v in sorted(outcome.items(),
                          key = operator.itemgetter(1),
                          reverse = True)[:10]:
            f.write(str(k) + "\t" +str(v) +'\n\n')


# In[ ]:





# In[ ]:





# In[ ]:




