
# coding: utf-8

# In[25]:


import pandas as pd;
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
nltk.download('punkt')


# In[10]:


a = pd.read_csv('data.csv',index_col='id', parse_dates=['created_time'], dtype={'name':np.str})


# In[78]:


a.name
hour = a.created_time
hour=hour.dt.hour
a['hour']=hour


# In[8]:


a.name.astype(np.str)


# In[12]:


a.name=a.name.astype(str)


# In[13]:


a.name


# In[35]:


a
a.name.values


# In[72]:


list= {"bar":"Club/Bistro/Cafe","social":"Causal/Hangout","disc":"Club/Bistro/Cafe","club":"Club/Bistro/Cafe","brewpub":"Club/Bistro/Cafe","brewery":"Club/Bistro/Cafe","cafe":"Club/Bistro/Cafe","restuarant":"Club/Bistro/Cafe","fort":"Historic","mahal":"Historic","dome":"Historic","village":"Historic","museum":"Historic","library":"Historic","mall":"Mall/Shopping Complex","market":"Mall/Shopping Complex","gate":"Mall/Shopping Complex","bowling":"Amusement Park/Activity","kart":"Amusement Park/Activity","karting":"Amusement Park/Activity","wonders":"Amusement Park/Activity","wonder":"Amusement Park/Activity","adventure":"Amusement Park/Activity","park":"Amusement Park/Activity","temple":"Worship/Temple","gurudwara":"Worship/Temple","sahib":"Worship/Temple","mosque":"Worship/Temple",
      "imax":"Movies/Cinema","pvr":"Movies/Cinema","cinema":"Movies/Cinema","theater":"Movies/Cinema","broadway":"Movies/Cinema",
      "garden":"Nature","hills":"Nature",
      "expo":"Exhibition","con":"Exhibition","bazar":"Exhibition","craft":"Exhibition"}
ade=[]
for i in a.name.values:
    blob = TextBlob(i)
    blob.words
    print(blob.words)
    k="";
    for j in blob.words:
        if(list.get(j.lower()) != None):
            print(list.get(j.lower()))
            k=list.get(j.lower());
        
    if(k == ""):
        k="Others"
    ade.append(k)


# In[73]:


for j in ade:
    print(j)


# In[74]:


a['type']=ade


# In[79]:


a


# In[126]:


ax=plt.figure(figsize=(20,15))

pl=sns.lmplot(size=8, y='hour',x='type', data=a,
           fit_reg=False, # No regression line
           hue='city')
pl.set_xticklabels(rotation=30)
fig = plt.figure()
fig.savefig('city.jpg')


# In[127]:


a.groupby('type').name.count().plot.bar()
fig.savefig('count.jpg')


# In[143]:


vpl=sns.violinplot(x='type', y='hour', data=a,inner=None,size=7)
labels=a.type
vpl.set_xticklabels(labels,rotation=30)
fig.savefig('density.jpg')

grp=a.groupby(['type'], as_index=False).sum()
grp=grp.sort_values(['hour'], ascending=[False]).groupby('type').head(5)
print(grp.head(6).type.values)
rr=grp.head(6).type.values
f= open("abc.txt","w+")
for i in rr:
    f.write(i)

