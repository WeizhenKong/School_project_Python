#!/usr/bin/env python
# coding: utf-8

# In[1]:


import operator
f1 = open("script01.txt","r")
f2 = open("script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()
s = s1+s2
s


# In[2]:


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


# In[3]:


outcome = {}
for word in outcome1:
        if word not in outcome:
            outcome[word] = 1
        else:
            outcome[word] += 1
outcome


# In[4]:


with open ("shradha.txt", 'a') as f:
        for k,v in sorted(outcome.items(),
                          key = operator.itemgetter(1),
                          reverse = True)[:10]:
            f.write(str(k) + "\t" +str(v) +'\n\n')


# In[ ]:




