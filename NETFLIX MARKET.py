#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[103]:


df = pd.read_csv('netflix.csv', index_col=0)


# In[104]:


df


# In[105]:


all_quarter_lst = list(df.index)


# In[106]:


quarter = []

for i in range(len(all_quarter_lst)):
    if 'quarter' in all_quarter_lst[i]:
        quarter.append(all_quarter_lst[i].replace('quarter',''))


# In[107]:


hbo_max = pd.read_csv('HBO MAX.csv', index_col=0)


# In[108]:


hbo_max


# In[109]:


disney_plus = pd.read_csv('Disney Plus.csv', index_col=0)


# In[110]:


disney_plus


# In[111]:


net_sub_lst = list(df['subscribers(millions)'])
hbo_sub_lst = list(hbo_max['subscribers(millions)'])
disney_sub_lst = list(disney_plus['subscribers(millions)'])


# In[112]:


# hbo_max 테이블 subscirbers(millions)인덱스의 마지막 value가 N/A였으므로 제거해준다
hbo_sub_lst = list(hbo_sub_lst[:-1])


# In[113]:


# 직선 그래프로 시각화하기 위하여 데이터가 없는 인덱스의 값에 0을 삽입한다
for i in range(len(net_sub_lst)-len(hbo_sub_lst)):
    hbo_sub_lst.insert(i, 0)
for i in range(len(net_sub_lst)-len(disney_sub_lst)):
    disney_sub_lst.insert(i, 0)


# In[114]:


hbo_sub_lst


# In[115]:


p1 = plt.plot(quarter, net_sub_lst, color='#2a9d8f', label='netflix')

plt.rcParams["figure.figsize"] = (10,5)
plt.xlabel('date')
plt.ylabel('subscriber(millions)')
plt.title('NETFLIX subscriber')
plt.figure(figsize=(50,40))
plt.show()


# In[116]:


p1 = plt.plot(quarter, net_sub_lst, color='#2a9d8f', label='netflix')
p2 = plt.plot(quarter, hbo_sub_lst, color='#e9c46a', label='hbo max')
p3 = plt.plot(quarter, disney_sub_lst, color='#e76f51', label='disney plus')
plt.legend((p1[0], p3[0], p2[0]),('netflix','disney plus','hbo max'), fontsize=5)

plt.rcParams["figure.figsize"] = (10,5)
plt.xlabel('date')
plt.ylabel('subscriber(millions)')
plt.title('OTT subscriber')
plt.figure(figsize=(50,40))
plt.show()


# In[117]:


j = 0
quarter_list=[]

for i in range(len(df)//2): 
    per = ((df['subscribers(millions)'][j+2] - (df['subscribers(millions)'][j])) / df['subscribers(millions)'][j]) * 100
    quarter_list.append(df.index[j])
    j = j+2


# In[118]:


quarter_list


# In[119]:


for i in range(len(net_sub_increase_list) - len(disney_plus_sub_increase_list)):
    disney_plus_sub_increase_list.insert(i, 0)

for i in range(len(net_sub_increase_list) - len(hbo_max_sub_increase_list)):
    hbo_max_sub_increase_list.insert(i, 0)


# In[120]:


# 구독자의 증가율을 시각화 하기 위해서 현재 분기점과 다음 분기점의 값을 사용하여 구독자 증가율을 계산한다.

j = 0
net_sub_increase_list = []

for i in range(len(net_sub_lst) // len(net_sub_lst[j:j+1])):
    
    if len(net_sub_lst[j:j+2]) == 2:
        net_sub_increase = (((net_sub_lst[j+1] - net_sub_lst[j]) / net_sub_lst[j]) * 100)
        net_sub_increase_list.append(net_sub_increase)
        
    j = j + 1


# In[121]:


net_sub_increase_list


# In[122]:


j = 0
disney_plus_sub_increase_list = []

for i in range(len(disney_sub_lst) // len(disney_sub_lst[j:j+1])):
    
    if len(disney_sub_lst[j:j+2]) == 2:
        try:
            disney_plus_sub_increase_list.append(((disney_sub_lst[j+1] - disney_sub_lst[j]) / disney_sub_lst[j]) * 100)
        except:
            disney_plus_sub_increase_list.append(0)
        
    j = j + 1


# In[123]:


disney_plus_sub_increase_list


# In[124]:


j = 0
hbo_max_sub_increase_list = []

for i in range(len(hbo_sub_lst) // len(hbo_sub_lst[j:j+1])):
    
    if len(hbo_sub_lst[j:j+2]) == 2:
        try:
            hbo_max_sub_increase_list.append(((hbo_sub_lst[j+1] - hbo_sub_lst[j]) / hbo_sub_lst[j]) * 100)
        except:
            hbo_max_sub_increase_list.append(0)
        
    j = j + 1


# In[125]:


disney_plus_sub_increase_list


# In[126]:


net_sub_increase_list.insert(0, 0)


# In[127]:


p1 = plt.plot(quarter[:-1], disney_plus_sub_increase_list, color='#e76f51', label='disney plus')
p2 = plt.plot(quarter[0:], net_sub_increase_list, color='#2a9d8f', label='netflix')
p3 = plt.plot(quarter[:-1], hbo_max_sub_increase_list, color='#e9c46a', label='hbo max')

plt.legend((p2[0], p1[0], p3[0]),('netflix', 'disney plus', 'hbo max'), fontsize=5)
plt.xlabel('date')
plt.ylabel('subscribers rate of increase')
plt.title('OTT subscriber rate of increase')
plt.figure(figsize=(50,40))
plt.show()


# In[128]:


plt.plot(quarter[0:], net_sub_increase_list, color='#2a9d8f', label='netflix')

plt.xlabel('date')
plt.ylabel('subscribers rate of increase')
plt.title('NETFLIX subsribers rate of increase')
plt.figure(figsize=(50,40))
plt.show()


# In[ ]:




