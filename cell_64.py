#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print(data.columns)
print('\n'*3)
print(data[['#','Name','Speed','Legendary']][0:6])
print('\n'*3)
print(data.iloc[4,9])
# print('\n'*3)
# for index,row in data.iterrows():
#   print(index,row['Speed'])
# print('\n'*3)
# data.loc[data["Speed"] > 100]
# print('\n'*3)
data.describe()

