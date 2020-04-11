#!/usr/bin/env python
# coding: utf-8

# In[1]:


f1 = open("script01.txt","r")
f2 = open("script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()
s = s1+s2
s


# In[2]:


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


# In[3]:


with open ("parta.txt", 'a') as f:
        for k,v in outcome.items():
            f.write(str(k) + "\t" +str(v) +'\n\n')


# In[ ]:




